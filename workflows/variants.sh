#!/usr/bin/env bash
# Paired short-read germline teaching workflow; Linux/WSL + biolab-raw env.
set -euo pipefail
if [[ $# -lt 6 || $# -gt 7 ]]; then
  echo 'Usage: variants.sh reference.fa R1.fastq.gz R2.fastq.gz sample output_dir ploidy [compatible_genes.gff3]' >&2
  exit 2
fi
ref=$(realpath "$1"); r1=$(realpath "$2"); r2=$(realpath "$3"); sample=$4; out=$5; ploidy=$6; gff=${7:-}
[[ $sample =~ ^[A-Za-z0-9_.-]+$ ]] || { echo 'Unsafe sample ID' >&2; exit 2; }
[[ $ploidy == 1 || $ploidy == 2 ]] || { echo 'Set explicit ploidy 1 or 2' >&2; exit 2; }
for tool in bwa samtools bcftools fastqc multiqc cutadapt; do command -v "$tool" >/dev/null; done
[[ ! -e $out ]] || { echo 'Output already exists; choose a new run directory' >&2; exit 2; }
mkdir -p "$out"; out=$(realpath "$out")
exec > >(tee "$out/run.log") 2>&1
threads=${THREADS:-4}
sha256sum "$ref" "$r1" "$r2" > "$out/inputs.sha256"
samtools --version > "$out/samtools.version.txt"; bcftools --version > "$out/bcftools.version.txt"
mkdir "$out/qc_raw" "$out/qc_clean"
fastqc -t "$threads" -o "$out/qc_raw" "$r1" "$r2"
# Supply adapter sequences only when the library kit/QC confirms them.
adapter_args=()
if [[ -n ${ADAPTER_R1:-} && -n ${ADAPTER_R2:-} ]]; then adapter_args=(-a "$ADAPTER_R1" -A "$ADAPTER_R2"); fi
cutadapt -j "$threads" -q 20 -m 30 "${adapter_args[@]}" -o "$out/R1.clean.fq.gz" -p "$out/R2.clean.fq.gz" "$r1" "$r2" > "$out/cutadapt.txt"
fastqc -t "$threads" -o "$out/qc_clean" "$out/R1.clean.fq.gz" "$out/R2.clean.fq.gz"
# Index a run-local copy; never write beside the user's raw reference.
cp "$ref" "$out/reference.fa"; ref="$out/reference.fa"
bwa index "$ref"; samtools faidx "$ref"
bwa mem -t "$threads" -R "@RG\tID:${sample}\tSM:${sample}\tPL:ILLUMINA" "$ref" "$out/R1.clean.fq.gz" "$out/R2.clean.fq.gz" |
  samtools sort -n -@ "$threads" -o "$out/name_sorted.bam" -
samtools fixmate -m "$out/name_sorted.bam" "$out/fixmate.bam"
samtools sort -@ "$threads" -o "$out/coordinate.bam" "$out/fixmate.bam"
samtools markdup "$out/coordinate.bam" "$out/aligned.bam"
samtools index "$out/aligned.bam"; samtools flagstat "$out/aligned.bam" > "$out/flagstat.txt"
bcftools mpileup -Ou -f "$ref" -q 20 -Q 20 -a FORMAT/DP,FORMAT/AD "$out/aligned.bam" |
  bcftools call -m -v --ploidy "$ploidy" -Oz -o "$out/calls.vcf.gz"
bcftools norm -f "$ref" -m -any "$out/calls.vcf.gz" -Oz -o "$out/normalized.vcf.gz"
bcftools filter -s LowQual -e 'QUAL<20 || QUAL="."' "$out/normalized.vcf.gz" -Oz -o "$out/filtered.vcf.gz"
bcftools index -t "$out/filtered.vcf.gz"
if [[ -n $gff ]]; then
  sha256sum "$gff" >> "$out/inputs.sha256"
  bcftools csq -f "$ref" -g "$gff" "$out/filtered.vcf.gz" -Oz -o "$out/annotated.vcf.gz"
  bcftools index -t "$out/annotated.vcf.gz"
else
  echo 'Consequence annotation NOT RUN: provide compatible GFF3, or run VEP/SnpEff with matching assembly.' > "$out/annotation_status.txt"
fi
bcftools stats "$out/filtered.vcf.gz" > "$out/variant_stats.txt"
multiqc "$out" -o "$out/multiqc"
echo 'Completed read-to-VCF workflow. Apply truth-region benchmark and biological interpretation separately.'
