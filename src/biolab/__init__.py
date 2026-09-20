"""Public, stable sequence API; domain modules expose advanced methods."""

from .sequence import (
    Alignment,
    align,
    clean_dna,
    gc_content,
    motif_positions,
    reverse_complement,
    sequence_summary,
)

__version__ = "0.1.0"
__all__ = [
    "Alignment",
    "align",
    "clean_dna",
    "gc_content",
    "motif_positions",
    "reverse_complement",
    "sequence_summary",
    "__version__",
]
