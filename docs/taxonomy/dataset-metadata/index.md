# Dataset metadata

*Dimension of the taxonomy · a single change type*

Changes in the information that describes the dataset **as a whole**: source, licensing, file format, field delimiter, train/test split information and temporal characteristics.

Dataset-level metadata influences both the **selection** and the **operation** of ML pipelines, which is why these changes are part of the taxonomy.

## What changes

| Metadata aspect | Possible change | Typical pipeline implication |
|---|---|---|
| Source, licensing | Different provider or licence terms | The dataset may no longer be suitable for the ML task or legally reusable; may require **replacing the dataset** or changing the pipeline configuration. |
| File format, field delimiter | e.g. CSV → Parquet, `,` → `;` | Can break ingestion or preprocessing; requires modifying **data loading and preprocessing** components. |
| Train/test split | Redefined splits shipped with the dataset | Alters the evaluation process when splits come with the dataset rather than being defined by the data scientist; may require adjusting **evaluation procedures, experimental settings or validation strategies**. |
| Temporal characteristics | Different collection period or sampling frequency | May affect result quality; may require changes in **feature engineering, preprocessing or validation**, especially when time is used explicitly (e.g. rolling-window analyses). |

!!! example "Example"
    A new version of a dataset is published as Parquet instead of CSV. The loader fails before any model code runs, so the fix lives entirely in the **ingestion** step.

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **9 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D1, D2, D3, D4, D5, D6, D7, D8, D9.

<!-- END GENERATED:observed -->
