# Internal-related information

Differences in information that, despite being found outside the dataset itself, explains the content of the dataset and/or is relevant to process and interpret its data.

## Aspects covered

| Aspect | Possible difference | Typical pipeline implication |
|---|---|---|
| Language, modality | The language or the modality of the data changes | The dataset may no longer fit the task or the model; may require changes in **preprocessing or in the model**. |
| Temporal characteristics | Different data collection period or sampling frequency | May affect result quality; may require changes in **feature engineering, preprocessing or validation**, especially when time is used explicitly (e.g. rolling-window analyses). |
| Train/test split | Redefined splits shipped with the dataset | Alters the evaluation process when splits come with the dataset rather than being defined by the data scientist; may require adjusting **evaluation procedures, experimental settings or validation strategies**. |
| Description of categorical values | The documented order or meaning of the categories changes | The order and meaning of categories are usually provided externally, not in the data; may require updating **encodings** or the interpretation of results. |

!!! note "File format and delimiter"
    How the data are stored (file format, field delimiter) is not part of this node; see [Format](../storage/format.md).
