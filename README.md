# Datheon DS/ML Internship

Machine-learning projects from the Datheon Data Science & ML internship: feature
engineering, classification and regression models, and benchmarking with F1, ROC-AUC
and RMSE.

## Tasks

| # | Task | Level | Highlights | Folder |
|---|------|-------|-----------|--------|
| 1 | Multi-Class Benchmark Classification Pipeline (Iris / Wine) | Beginner | StandardScaler, Logistic Regression vs Decision Tree, confusion matrices, ROC curves | [task-01-multiclass-classification](task-01-multiclass-classification/) |

## Repository layout
```
Datheon-ds-ml-internship/
├── task-01-multiclass-classification/   # each task is self-contained
│   ├── data/  notebooks/  reports/  src/
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md
```

## Quick start
```bash
git clone https://github.com/patrira/Datheon-ds-ml-internship.git
cd Datheon-ds-ml-internship
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows  |  source .venv/bin/activate (macOS/Linux)
pip install -r task-01-multiclass-classification/requirements.txt
```
See each task's README for detailed instructions and results.

## Author
Patrick Iradukunda — Datheon DS/ML Intern
