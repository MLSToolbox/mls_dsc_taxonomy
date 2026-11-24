# Metadata

Differences in the information that describes the dataset **as a whole**: source, licensing, file format, field delimiter, train/test split information and temporal characteristics.

Dataset-level metadata influences both the **selection** and the **operation** of ML pipelines, which is why these changes are part of the taxonomy.


This node is documented as a **single, closed page**: its aspects are not described as separate change types.

## What changes

| Aspect | Possible difference | Typical pipeline implication |
|---|---|---|
| License | Different license terms | The dataset may no longer be legally reusable; may require **replacing the dataset** or changing the pipeline configuration. |
| Source | Different provider or origin | The dataset may no longer be suitable for the ML task; may require replacing it or changing the pipeline configuration. |
| Language, modality | The language or the modality of the data changes | The dataset may no longer fit the task or the model; may require changes in **preprocessing or in the model**. |
| Temporal characteristics | Different data collection period or sampling frequency | May affect result quality; may require changes in **feature engineering, preprocessing or validation**, especially when time is used explicitly (e.g. rolling-window analyses). |
| Train/test split | Redefined splits shipped with the dataset | Alters the evaluation process when splits come with the dataset rather than being defined by the data scientist; may require adjusting **evaluation procedures, experimental settings or validation strategies**. |
| Description of categorical values | The documented order or meaning of the categories changes | The order and meaning of categories are usually provided externally, not in the data; may require updating **encodings** or the interpretation of results. |

!!! example "Example"
    A new version of a dataset is published as Parquet instead of CSV. The loader fails before any model code runs, so the fix lives entirely in the **ingestion** step.

!!! note "File format and delimiter"
    How the data are stored (file format, field delimiter) is not part of this node; see [Format](storage/format.md).
