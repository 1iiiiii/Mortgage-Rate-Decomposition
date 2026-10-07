# Expectations of real interest rate and inflation expectations are driving up the rates

Published post: [https://1iiiiii.github.io/Personal-Website/blog/posts/post4/]

## Data

All FRED series are downloaded with `fredapi`; the ACM file is downloaded from the NY Fed with `requests` (access date: the run date of the fetch notebooks).

| Source | Series | What it contains | Native frequency | Period used |
|---|---|---|---|---|
| Freddie Mac PMMS | `MORTGAGE30US` | 30-year fixed mortgage rate | weekly (Thu) | 2000-01 to 2026-09 (Fig 1); 2003-01 onward elsewhere |
| Federal Reserve Board H.15 | `DGS10` | 10-year Treasury constant-maturity yield | daily | same as above |
| Federal Reserve Board H.15 | `DFII10` | 10-year TIPS yield (real), cross-check | daily | 2003-01 to 2026-09 |
| FRED (derived) | `T10YIE` | 10-year breakeven inflation (`DGS10` − `DFII10`), cross-check | daily | 2003-01 to 2026-09 |
| Federal Reserve Board H.4.1 | `WSHOMCB` | Fed holdings of agency MBS | weekly (Wed) | 2003-01 to 2026-09 |
| Federal Reserve Bank of Cleveland | `EXPINF10YR` | 10-year expected inflation | monthly | 2003-01 to 2026-09 |
| Federal Reserve Bank of Cleveland | `REAINTRATREARAT10Y` | 10-year real interest rate (includes the real risk premium) | monthly | 2003-01 to 2026-09 |
| Federal Reserve Bank of Cleveland | `TENEXPCHAREARISPRE` | 10-year real risk premium | monthly | 2003-01 to 2026-09 |
| Federal Reserve Bank of Cleveland | `TENEXPCHAINFRISPRE` | 10-year inflation risk premium | monthly | 2003-01 to 2026-09 |
| Federal Reserve Bank of New York | `ACMTermPremium.xls`, sheet *ACM Daily* (`ACMY10`, `ACMRNY10`, `ACMTP10`) | Adrian–Crump–Moench fitted 10-year yield, expected short-rate path and term premium; model cross-check | daily | 2003-01 to 2026-09 |

The Cleveland Fed series come from the Haubrich, Pennacchi & Ritchken (2012) term-structure model.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # FRED API key into .env
```

## Replication

| Notebook | Reads | Writes |
|---|---|---|
| `code/01_fetch_fred.ipynb` | FRED API | `data/raw/<SERIES_ID>.csv` (nine files) |
| `code/02_fetch_acm.ipynb` | NY Fed ACM Excel file | `data/raw/acm.csv` |
| `code/03_build_series.ipynb` | `data/raw/` | `data/processed/monthly.csv`, `data/processed/contributions.csv`, `results/tables/headline.csv`, `spread_stats.csv`, `residual.csv`, `contrib_shares.csv`, `model_crosscheck.csv` |
| `code/04_figures.ipynb` | `data/raw/`, `data/processed/` | `results/figures/fig1_levels.png`, `fig2_contributions.png`, `fig3_spread_drivers.png` |

## Layout

```
code/             numbered notebooks, run in order; plot_style.py holds the shared theme
data/raw/         as downloaded, never edited by hand
data/processed/   analysis-ready series
results/figures/  PNGs embedded in the post
results/tables/   every number quoted in the post
```
