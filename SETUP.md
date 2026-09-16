# Quraşdırma və təkrar icra

## Python — Windows / macOS / Linux

Python 3.12 ilə yoxlanıb. Repo kökündə:
```bash
python -m venv .venv
# Windows PowerShell:
.venv/Scripts/Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -e ".[dev,research]"
python -m pytest
python scripts/fetch_data.py --dataset all
python scripts/run_projects.py --project all
python scripts/protein_project.py
python scripts/make_visualizations.py
python scripts/check_repository.py
```

Shell activation məhduddursa `.venv/Scripts/python.exe` tam yolunu istifadə edin. Əsas asılılıqlar `pyproject.toml`, faktiki Windows/Python mühiti `requirements-tested.txt` faylındadır. Freeze faylı platformadan asılıdır; Linux üçün birbaşa kopyalamayın. Şəbəkəsiz testlər dataset endirmir.

## Notebook

```bash
python -m ipykernel install --user --name biolab --display-name "Bioinformatics Lab"
```
JupyterLab/VS Code-da `biolab` kernel seçin. Notebook-lar unexecuted tədqiqat şablonu deyil: əsas modulları çağırır, output-u interpretasiya bölməsinə bağlayır. İcra statusu STATUS-da göstərilir. İstəyə görə `python -m pip install jupyterlab`.

## Xam sequencing

Linux/WSL və Conda/Mamba tələb olunur:
```bash
conda env create -f workflows/environment.yml
conda activate biolab-raw
```
Bu Conda YAML alternativ lokal quraşdırma reseptidir; CI-də yoxlanmış quraşdırma
[raw-examples.yml](.github/workflows/raw-examples.yml)-dəki Conda + Ubuntu + pip
addımlarıdır. Artifact faktiki versiyaları saxlayır. Genome index böyük RAM/disk
tələb edə bilər; kiçik genomla başlayın. [Workflow təlimatı](workflows/README.md)
input və parametr şərtlərini verir.

Windows-da Linux quraşdırmadan sınaq üçün GitHub-da **Actions → Real raw-read
examples → Run workflow** seçin. Linux olan maşında eyni icra:

```bash
python -m pip install -e '.[research]' 'multiqc>=1.27,<2'
python scripts/run_raw_examples.py --output results/runs/raw-examples-001
```

## Tipik problemlər

- “Counts and metadata sample IDs differ”: sample ID-ləri düzəldin; sıraya görə zorla uyğunlaşdırmayın.
- Endirmədə HTTP error: URL/release və xidmət statusunu yoxlayın; data kartında yeni versiya açın.
- Checksum mismatch: fayl dəyişib; əvvəlki nəticəni dəyişmiş input-la eyni saymayın.
- RNA model convergence xəbərdarlığı: design rank, az count, outlier və replikatları audit edin; xəbərdarlığı gizlətməyin.
- `pysam` Windows: HTS işlərini Linux/WSL-də edin; Python text VCF analizinə bu paket lazım deyil.
