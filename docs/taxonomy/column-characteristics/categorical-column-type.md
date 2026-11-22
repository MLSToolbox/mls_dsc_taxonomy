# Categorical column type

*Dimension: [Column characteristics](index.md)*

## What changes

The data type of a categorical column changes. Examples: encoding categorical variables as booleans through one-hot encoding, or transforming numerical columns into categorical ones and vice versa.

## Pipeline implications

Different ML algorithms and pipeline components rely on specific data representations, so a new representation may not be accepted or may be interpreted differently.

## Typical adaptation

Data preprocessing, feature engineering and model configuration.

See also: [Numerical column type](numerical-column-type.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **2 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D3, D4.

<!-- END GENERATED:observed -->
