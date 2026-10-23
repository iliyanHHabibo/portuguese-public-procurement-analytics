# Data sources

## Contratos Públicos – Portal BASE (IMPIC)

| | |
|---|---|
| Dataset | Contratos Públicos – Portal BASE – IMPIC – contratos de 2012 a 2026 |
| URL | https://dados.gov.pt/en/datasets/contratos-publicos-portal-base-impic-contratos-de-2012-a-2026/ |
| Publisher | IMPIC, via dados.gov.pt |
| Licence | Public domain |
| Update frequency (per source) | Every two weeks |
| Downloaded | 2026-10-13 |
| Format | JSON, one file per year |
| Years used | 2022–2026 |

## Snapshot row counts

| File | Rows |
|---|---:|
| contratos2022 | 176,603 |
| contratos2023 | 194,009 |
| contratos2024 | 227,464 |
| contratos2025 | 247,828 |
| contratos2026 | 189,783 |
| **Total** | **1,035,687** |

These counts are the baseline for the first data quality check (bronze table row count per source file = count above).

## Notes

- The source is updated regularly, so a later download will not match these counts (especially 2026). Re-downloads must record a new date and new counts.
- Raw files are stored in OneLake (`lh_bronze`, `Files/base/contratos/<year>/`), not in Git.
