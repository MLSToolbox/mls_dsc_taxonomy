# Numerical column values

*Dimension: [Column characteristics](index.md)*

## What changes

Two kinds of change fall here:

- **Transformations of scale or distribution:** multiplicative factors, logarithmic transformations, normalisation techniques (min-max scaling, standardisation) or value perturbation for obfuscation purposes.
- **Representation changes:** the decimal separator (dot or comma), standard vs. scientific notation, or the encoding format of numerical values.

## Pipeline implications

Scale and distribution changes affect feature scaling and model behaviour. Representation changes may leave the underlying semantics intact but can still break parsing.

## Typical adaptation

Preprocessing steps, feature scaling procedures or model retraining for the first kind; data ingestion or parsing components for the second.

See also: [Categorical column values](categorical-column-values.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **1 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D8.

<!-- END GENERATED:observed -->
