# Numerical Column Type (C321)

**Perspective:** [Column Characteristics](../perspectives/column-characteristics.md)

## Description

Changes affecting the data type of numerical columns.

## Examples

An example is converting real-valued numbers into integers. The paper also discusses transformations between numerical and categorical columns as column data-type changes. Numerical columns may additionally undergo representation changes, such as modifying the decimal separator (dot or comma), changing between standard and scientific notation, or altering the encoding format of numerical values.

## Potential implications for ML pipeline evolution

Changes to column data types may require adaptations in data preprocessing, feature engineering, and model configuration, as different ML algorithms and pipeline components may rely on specific data representations. Numerical representation changes may not affect the underlying semantics of the data, but may require modifications to data ingestion or parsing components.
