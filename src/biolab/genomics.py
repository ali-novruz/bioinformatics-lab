"""Descriptive VCF analysis, not clinical variant classification."""
from collections import Counter
import re
import pandas as pd
from .io import read_vcf

def variant_type(ref,alt):
    if alt in {".","*"}: return "nonvariant_or_spanning_deletion"
    if alt.startswith("<") or "[" in alt or "]" in alt: return "structural_or_symbolic"
    if len(ref)==len(alt)==1: return "SNV"
    if len(ref)!=len(alt): return "indel"
    return "MNV"

def allele_counts(samples, n_alt):
    counts=[0]*(n_alt+1)
    for value in samples.values():
        gt=value.get("GT",".")
        for token in re.split(r"[/|]",gt):
            if token==".": continue
            i=int(token)
            if i<0 or i>n_alt: raise ValueError(f"GT allele out of range: {gt}")
            counts[i]+=1
    return counts

def analyze_vcf(path, min_qual=20, require_pass=True):
    rows=[]; total=0;reasons=Counter();ti=tv=0
    for rec in read_vcf(path):
        total+=1
        if require_pass and rec['filter']!='PASS': reasons['not_PASS']+=1;continue
        if min_qual is not None and (rec['qual'] is None or rec['qual']<min_qual): reasons['low_or_missing_QUAL']+=1;continue
        counts=allele_counts(rec['samples'],len(rec['alts']))
        an=sum(counts)
        for idx,alt in enumerate(rec['alts'],1):
            kind=variant_type(rec['ref'],alt)
            if kind=='SNV' and {rec['ref'],alt}<=set('ACGT') and rec['ref']!=alt:
                if {rec['ref'],alt} in ({'A','G'},{'C','T'}):ti+=1
                else:tv+=1
            rows.append({"chrom":rec['chrom'],"pos":rec['pos'],"ref":rec['ref'],"alt":alt,"type":kind,"qual":rec['qual'],"filter":rec['filter'],"called_alleles":an,"alt_alleles":counts[idx],"sample_alt_frequency":counts[idx]/an if an else None})
    columns=['chrom','pos','ref','alt','type','qual','filter','called_alleles','alt_alleles','sample_alt_frequency']
    table=pd.DataFrame(rows,columns=columns)
    summary={"input_records":total,"retained_alleles":len(rows),"excluded_records":dict(reasons),"types":dict(Counter(r['type'] for r in rows)),"transitions":ti,"transversions":tv,"ti_tv":ti/tv if tv else None,"min_qual":min_qual,"require_PASS":require_pass}
    return table,summary
