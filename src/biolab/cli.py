"""Small command-line interface. All file paths are explicit."""
import argparse,json
from pathlib import Path
from .sequence import align,sequence_summary
from .io import read_fasta
from .genomics import analyze_vcf

def main():
    p=argparse.ArgumentParser(description='Bioinformatics teaching and analysis tools')
    sub=p.add_subparsers(dest='command',required=True)
    dna=sub.add_parser('dna');dna.add_argument('fasta')
    aln=sub.add_parser('align');aln.add_argument('query');aln.add_argument('target');aln.add_argument('--mode',choices=['global','local'],default='global')
    vcf=sub.add_parser('variants');vcf.add_argument('vcf');vcf.add_argument('--output',required=True);vcf.add_argument('--min-qual',type=float,default=20)
    args=p.parse_args()
    if args.command=='dna':out={name:sequence_summary(seq) for name,seq in read_fasta(args.fasta)}
    elif args.command=='align':out=align(args.query,args.target,args.mode).to_dict()
    else:
        table,out=analyze_vcf(args.vcf,args.min_qual)
        dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True);table.to_csv(dest,index=False)
    print(json.dumps(out,indent=2,ensure_ascii=False,allow_nan=False))

if __name__=='__main__':main()
