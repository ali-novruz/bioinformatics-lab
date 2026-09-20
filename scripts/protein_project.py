"""Real UniProt sequence and PDB structure examples, with distinct identities."""

from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
from Bio.PDB import PDBParser

from biolab.reporting import new_run, write_json

ROOT = Path(__file__).resolve().parents[1]


def run():
    fasta = ROOT / "datasets/raw/P01308.fasta"
    pdb = ROOT / "datasets/raw/1CRN.pdb"
    out = new_run(ROOT, "proteins", [fasta, pdb], {"contact_cutoff_angstrom": 8})
    record = SeqIO.read(fasta, "fasta")
    structure = PDBParser(QUIET=True).get_structure("1CRN", pdb)
    residues = [r for r in structure[0]["A"] if r.id[0] == " " and "CA" in r]
    xyz = np.array([r["CA"].coord for r in residues])
    distances = np.linalg.norm(xyz[:, None, :] - xyz[None, :, :], axis=-1)
    contacts = (distances < 8) & (distances > 0)
    if not np.allclose(distances, distances.T) or not np.allclose(
        np.diag(distances), 0
    ):
        raise AssertionError("Invalid distances")
    np.savetxt(out / "ca_distances.csv", distances, delimiter=",")
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(distances, cmap="viridis_r")
    ax.set(
        xlabel="Chain A residue index",
        ylabel="Chain A residue index",
        title="1CRN experimental Cα distances (Å)",
    )
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(out / "contact_map.png", dpi=160)
    plt.close(fig)
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(*xyz.T, c="#157f83")
    ax.scatter(*xyz.T, c=np.arange(len(xyz)), cmap="viridis", s=16)
    ax.set(
        xlabel="X (Å)",
        ylabel="Y (Å)",
        zlabel="Z (Å)",
        title="1CRN chain A: Cα trace, not atomic surface",
    )
    fig.tight_layout()
    fig.savefig(out / "protein_structure.png", dpi=160)
    plt.close(fig)
    write_json(
        out / "summary.json",
        {
            "uniprot_accession": "P01308",
            "protein": "human insulin precursor",
            "sequence_length": len(record.seq),
            "composition": dict(Counter(str(record.seq))),
            "pdb": "1CRN",
            "structure_protein": "crambin; NOT the insulin sequence",
            "chain": "A",
            "ca_residues": len(residues),
            "undirected_ca_contacts_lt8A": int(np.triu(contacts, 1).sum()),
            "contact_definition": "all nonidentical CA pairs <8 Angstrom, including sequence neighbours; not chemical bonds",
        },
    )
    return out


if __name__ == "__main__":
    print(run())
