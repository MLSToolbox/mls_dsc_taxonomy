# Categorical column values

*Dimension: [Column characteristics](index.md)*

## What changes

The set of values represented in a categorical column changes: categories are **added or removed**, or **mappings are applied**, for instance to anonymise existing values.

## Pipeline implications

Encoders trained on the previous categories may fail or silently mis-encode unseen or missing values.

## Typical adaptation

Update encoding strategies, validation rules or model inputs.

See also: [Numerical column values](numerical-column-values.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **5 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D3, D4, D7, D8, D9.

<!-- END GENERATED:observed -->
