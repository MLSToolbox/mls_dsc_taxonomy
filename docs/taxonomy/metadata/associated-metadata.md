# Associated metadata

Information that describes the dataset **as a whole** rather than its content, and that is needed to interpret it and to decide whether it is suitable for an ML task.

It is the only change type of the [Metadata](index.md) dimension, and it is documented as a **single, closed page**: its aspects are not described as separate change types.

## Aspects covered

| Aspect | Possible difference | Typical pipeline implication |
|---|---|---|
| License | Different license terms | The dataset may no longer be legally reusable; may require **replacing the dataset** or changing the pipeline configuration. |
| Source | Different provider or origin | The dataset may no longer be suitable for the ML task; may require replacing it or changing the pipeline configuration. |
| Language, modality | The language or the modality of the data changes | The dataset may no longer fit the task or the model; may require changes in **preprocessing or in the model**. |
| Temporal characteristics | Different data collection period or sampling frequency | May affect result quality; may require changes in **feature engineering, preprocessing or validation**, especially when time is used explicitly (e.g. rolling-window analyses). |
| Train/test split | Redefined splits shipped with the dataset | Alters the evaluation process when splits come with the dataset rather than being defined by the data scientist; may require adjusting **evaluation procedures, experimental settings or validation strategies**. |
| Description of categorical values | The documented order or meaning of the categories changes | The order and meaning of categories are usually provided externally, not in the data; may require updating **encodings** or the interpretation of results. |

!!! example "Example"
    A new version relicenses the data under non-commercial terms. Not a single file changes, but a pipeline that was legitimately using the dataset may no longer be able to do so.

!!! note "File format and delimiter"
    How the data are stored (file format, field delimiter) is not part of this node; see [Format](../storage/format.md).
