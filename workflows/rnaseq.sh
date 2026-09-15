#!/usr/bin/env bash
# STAR + featureCounts for a single RNA-seq sample; combine via combine_counts.py.
set -euo pipefail
if [[ $# != 7 ]]; then
  echo 'Usage: rnaseq.sh genome.fa genes.gtf R1.fastq.gz R2.fastq.gz_OR_NONE sample out_dir strandedness_0_1_2' >&2; exit 2
fi
ref=$(realpath "$1"); gtf=$(realpath "$2"); r1=$(realpath "$3"); r2=$4; sample=$5; out=$6; strand=$7
[[ $sample =~ ^[A-Za-z0-9_.-]+$ && $strand =~ ^[012]$ ]] || exit 2
[[ ! -e $out ]] || { echo 'Output exists; select a new run directory' >&2; exit 2; }
for tool in STAR featureCounts fastqc multiqc samtools; do command -v "$tool" >/dev/null; done
mkdir -p "$out"; out=$(realpath "$out");mkdir "$out/index" "$out/qc"
exec > >(tee "$out/run.log") 2>&1
threads=${THREADS:-4}; overhang=${SJDB_OVERHANG:-99}
reads=("$r1");paired=()
if [[ $r2 != NONE ]]; then r2=$(realpath "$r2");reads+=("$r2");paired=(-p --countReadPairs);fi
sha256sum "$ref" "$gtf" "${reads[@]}" > "$out/inputs.sha256"
STAR --version > "$out/STAR.version.txt"
fastqc -t "$threads" -o "$out/qc" "${reads[@]}"
STAR --runThreadN "$threads" --runMode genomeGenerate --genomeDir "$out/index" --genomeFastaFiles "$ref" --sjdbGTFfile "$gtf" --sjdbOverhang "$overhang"
STAR --runThreadN "$threads" --genomeDir "$out/index" --readFilesIn "${reads[@]}" --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix "$out/${sample}."
bam="$out/${sample}.Aligned.sortedByCoord.out.bam"
samtools index "$bam"
featureCounts -T "$threads" "${paired[@]}" -s "$strand" -t exon -g gene_id -a "$gtf" -o "$out/${sample}.counts.tsv" "$bam"
multiqc "$out" -o "$out/multiqc"
echo 'Join all biological samples by gene ID, then run the count-model with explicit metadata.'
