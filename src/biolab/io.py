"""Validated streaming parsers for teaching-sized FASTA and text VCF."""
from pathlib import Path
import gzip
import math
from Bio import SeqIO
from .sequence import clean_dna

def text_open(path):
    return gzip.open(path,"rt",encoding="utf-8") if str(path).endswith(".gz") else open(path,encoding="utf-8")

def read_fasta(path):
    seen=set()
    with text_open(path) as f:
        for rec in SeqIO.parse(f,"fasta"):
            if rec.id in seen: raise ValueError(f"Duplicate FASTA ID: {rec.id}")
            if not rec.seq: raise ValueError(f"Empty FASTA record: {rec.id}")
            seen.add(rec.id)
            yield rec.id,clean_dna(str(rec.seq))
    if not seen: raise ValueError(f"No FASTA records in {path}")

def read_vcf(path):
    """Preserve multi-allelic records. Not a full BCF/SV normalization library."""
    header=None
    with text_open(path) as f:
        for lineno,line in enumerate(f,1):
            if line.startswith("##") or not line.strip(): continue
            if line.startswith("#CHROM"):
                if header is not None: raise ValueError('Duplicate #CHROM header')
                header=line.rstrip().split("\t")
                if header[:8]!=["#CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO"]:
                    raise ValueError("Invalid VCF column header")
                if len(header)==9 or (len(header)>8 and header[8]!='FORMAT'):
                    raise ValueError('VCF sample columns require FORMAT and sample names')
                if len(set(header[9:]))!=len(header[9:]) or any(not name.strip() for name in header[9:]):
                    raise ValueError('Duplicate or empty VCF sample names')
                continue
            if line.startswith("#"): continue
            if header is None: raise ValueError("Missing #CHROM header")
            fields=line.rstrip("\n\r").split("\t")
            if len(fields)!=len(header): raise ValueError(f"Wrong field count on line {lineno}")
            chrom,pos,vid,ref,alt,qual,filt,info=fields[:8]
            pos=int(pos)
            if pos<1 or not ref: raise ValueError(f"Invalid position/reference on line {lineno}")
            quality=None if qual=="." else float(qual)
            if quality is not None and (not math.isfinite(quality) or quality<0): raise ValueError("Invalid QUAL")
            attrs={}
            if info!=".":
                for item in info.split(";"):
                    key,sep,value=item.partition("=")
                    attrs[key]=value if sep else True
            samples={}
            if len(fields)>8:
                keys=fields[8].split(":")
                if len(set(keys))!=len(keys) or any(not k or k=='.' for k in keys):
                    raise ValueError('Invalid or duplicate FORMAT keys')
                if 'GT' in keys and keys[0]!='GT': raise ValueError('GT must be the first FORMAT field')
                for name,value in zip(header[9:],fields[9:]):
                    values=value.split(':')
                    if len(values)>len(keys) or any(v=='' for v in values):
                        raise ValueError(f'Invalid sample FORMAT values on line {lineno}')
                    # VCF permits omitted trailing sample fields; preserve them as missing.
                    values += ['.']*(len(keys)-len(values))
                    samples[name]=dict(zip(keys,values))
            yield {"chrom":chrom,"pos":pos,"id":vid,"ref":ref,"alts":tuple(alt.split(",")),"qual":quality,"filter":filt,"info":attrs,"samples":samples}
    if header is None: raise ValueError("Missing #CHROM header")
