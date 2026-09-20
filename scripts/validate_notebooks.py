"""Execute every notebook; retain fresh copies without overwriting published evidence."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient

from biolab.reporting import recorded_run, write_json

ROOT = Path(__file__).resolve().parents[1]


def main():
    notebooks = sorted((ROOT / "notebooks").rglob("*.ipynb"))
    with recorded_run(
        ROOT, "notebook-validation", notebooks, {"cell_timeout_seconds": 300}
    ) as out:
        completed = []
        for path in notebooks:
            print(f"Executing {path.name}", flush=True)
            notebook = nbformat.read(path, as_version=4)
            NotebookClient(
                notebook,
                timeout=300,
                kernel_name="python3",
                resources={"metadata": {"path": str(ROOT)}},
            ).execute()
            nbformat.write(notebook, out / path.name)
            completed.append(path.relative_to(ROOT).as_posix())
            write_json(
                out / "summary.json", {"completed": completed, "count": len(completed)}
            )
    print(out, flush=True)


if __name__ == "__main__":
    main()
