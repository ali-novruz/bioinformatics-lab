"""Check the separation and execution state of teaching and reproduction notebooks."""

from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    learn = sorted((ROOT / "notebooks/learn").glob("*.ipynb"))
    reproduce = sorted((ROOT / "notebooks/reproduce").glob("*.ipynb"))
    assert len(learn) == len(reproduce) == 8
    for path in learn:
        notebook = nbformat.read(path, as_version=4)
        code = [cell for cell in notebook.cells if cell.cell_type == "code"]
        assert len(notebook.cells) >= 24, path
        assert len(code) >= 8, path
        assert all(cell.execution_count is not None for cell in code), path
        assert sum(bool(cell.outputs) for cell in code) >= 7, path
    for path in reproduce:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
    print(
        "8 guided notebooks (24+ cells, executed) and 8 reproduction notebooks verified"
    )


if __name__ == "__main__":
    main()
