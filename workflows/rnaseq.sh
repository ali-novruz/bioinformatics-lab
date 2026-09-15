#!/usr/bin/env bash
# STAR + featureCounts for a single RNA-seq sample; combine via combine_counts.py.
set -euo pipefail
if [[ $# != 7 ]]; then
  echo 'Usage: rnaseq.sh genome.fa genes.gtf R1.fastq.gz R2.fastq.gz_OR_NONE sample out_dir strandedness_0_1_2' >&2; exit 2
fi
ref=$(realpath "$1"); gtf=$(realpath "$2"); r1=$(realpath "$3"); r2=$4; sample=$5; out=$6; strand=$7
[[ $sample =~ ^[A-Za-z0-9_.-]+$ && $strand =~ ^[012]$ ]] || exit 2
[[ ! -e $out ]] || { echo 'Output exists; select a new run directory' >&2; exit 2; }
for tool in STAR featureCounts samtools; do command -v "$tool" >/dev/null; done
if [[ ${SKIP_QC:-0} != 1 ]]; then command -v fastqc >/dev/null; fi
if [[ ${SKIP_MULTIQC:-0} != 1 ]]; then command -v multiqc >/dev/null; fi
mkdir -p "$out"; out=$(realpath "$out");mkdir "$out/index"; if [[ ${SKIP_QC:-0} != 1 ]]; then mkdir "$out/qc"; fi
exec > >(tee "$out/run.log") 2>&1
threads=${THREADS:-4}; overhang=${SJDB_OVERHANG:-99}
reads=("$r1");paired=()
if [[ $r2 != NONE ]]; then r2=$(realpath "$r2");reads+=("$r2");paired=(-p --countReadPairs);fi
sha256sum "$ref" "$gtf" "${reads[@]}" > "$out/inputs.sha256"
STAR --version > "$out/STAR.version.txt"
if [[ ${SKIP_QC:-0} != 1 ]]; then fastqc -t "$threads" -o "$out/qc" "${reads[@]}"; fi
star_index_args=()
if [[ -n ${STAR_SA_INDEX_NBASES:-} ]]; then star_index_args+=(--genomeSAindexNbases "$STAR_SA_INDEX_NBASES"); fi
STAR --runThreadN "$threads" --runMode genomeGenerate --genomeDir "$out/index" --genomeFastaFiles "$ref" --sjdbGTFfile "$gtf" --sjdbOverhang "$overhang" "${star_index_args[@]}"
STAR --runThreadN "$threads" --genomeDir "$out/index" --readFilesIn "${reads[@]}" --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix "$out/${sample}."
bam="$out/${sample}.Aligned.sortedByCoord.out.bam"
samtools index "$bam"
featureCounts -T "$threads" "${paired[@]}" -s "$strand" -t exon -g gene_id -a "$gtf" -o "$out/${sample}.counts.tsv" "$bam"
if [[ ${SKIP_MULTIQC:-0} != 1 ]]; then multiqc "$out" -o "$out/multiqc"; fi
echo 'Join all biological samples by gene ID, then run the count-model with explicit metadata.'
