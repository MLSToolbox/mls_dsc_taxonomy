# Remove column

*Dimension: [Columns set](../index.md)*

## What changes

An existing column disappears from the dataset.

## Pipeline implications

The pipeline fails if the removed column is **explicitly required**, for example as a feature, as the target, or in a preprocessing step.

## Typical adaptation

Modify feature engineering steps, model inputs, or retraining procedures, or replace the dataset if the column is essential.

See also: [Add column](add-column.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **4 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D4, D7, D8, D9.

<!-- END GENERATED:observed -->
