"""Canonical start-to-first-stop ORFs on both strands, including circular origins."""
from Bio.Seq import Seq
from .sequence import clean_dna,reverse_complement


def find_orfs(sequence,min_aa=30,circular=False):
    sequence=clean_dna(sequence)
    if not sequence or set(sequence)-set('ACGT'):
        raise ValueError('Nonempty unambiguous ACGT sequence required')
    if not isinstance(min_aa,int) or min_aa<1:raise ValueError('Positive integer min_aa required')
    length=len(sequence); found=[]
    for strand,oriented in [('+',sequence),('-',reverse_complement(sequence))]:
        extended=oriented+oriented if circular else oriented
        for start in range(length):
            if extended[start:start+3]!='ATG':continue
            limit=start+length if circular else length
            for stop in range(start+3,limit-2,3):
                if extended[stop:stop+3] not in {'TAA','TAG','TGA'}:continue
                end=stop+3; coding=extended[start:stop]
                if len(coding)//3>=min_aa:
                    oriented_segments=[(start,min(end,length))]+([(0,end-length)] if end>length else [])
                    segments=oriented_segments if strand=='+' else [(length-b,length-a) for a,b in oriented_segments]
                    protein=str(Seq(coding).translate(table=1))
                    found.append({'strand':strand,'oriented_start0':start,'frame_offset':start%3,
                                  'segments0':segments,'wraps_origin':end>length,'length_nt_with_stop':end-start,
                                  'length_aa':len(protein),'stop_codon':extended[stop:end],'protein':protein})
                break
    return sorted(found,key=lambda r:(r['strand'],r['oriented_start0']))
