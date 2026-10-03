# [WRITE headline: the finding, not the topic]

[WRITE one or two sentences on the question this repository answers.]

Published post: [WRITE link to the post on https://1iiiiii.github.io/Personal-Website/]

## Data

| Source | Series / file | What it contains | Access | Period |
|---|---|---|---|---|
| FRED (St. Louis Fed) | `MORTGAGE30US` | 30-year fixed mortgage rate, weekly (Freddie Mac PMMS) | `fredapi` | [WRITE] |
| FRED | `DGS10` | 10-year Treasury constant-maturity yield, daily | `fredapi` | [WRITE] |
| FRED | `DFII10` | 10-year TIPS yield (real), daily | `fredapi` | [WRITE] |
| FRED | `T10YIE` | 10-year breakeven inflation, daily | `fredapi` | [WRITE] |
| FRED | `WSHOMCB` | Fed holdings of agency MBS, weekly | `fredapi` | [WRITE] |
| NY Fed | ACM term premium | 10-year expected short rate and term premium | CSV from URL | [WRITE] |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # then paste your FRED API key into .env
```

## Replication

Run the scripts in order from the repository root:

| Script | Reads | Writes |
|---|---|---|
| `code/01_fetch_fred.py` | FRED API | [WRITE] |
| `code/02_fetch_acm.py` | NY Fed CSV | [WRITE] |
| `code/03_build_series.py` | `data/raw/` | [WRITE] |
| `code/04_figures.py` | `data/processed/` | `results/figures/fig1–3.png`, `results/tables/` |

## Layout

```
code/             numbered scripts, run in order; plot_style.py holds the shared theme
data/raw/         as downloaded, never edited by hand
data/processed/   analysis-ready series
results/figures/  PNGs embedded in the post
results/tables/   every number quoted in the post
```
