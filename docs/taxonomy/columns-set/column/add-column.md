# Add column

*Dimension: [Columns set](../index.md)*

## What changes

A new column is introduced into the dataset.

## Pipeline implications

Modifies the input data available to the pipeline. Automatic feature selection mechanisms may be affected by the new attribute.

## Typical adaptation

Incorporate the new attribute into the pipeline when it is relevant, or adjust feature selection steps so that it is handled (or deliberately ignored).

See also: [Remove column](remove-column.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **2 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D5, D8.

<!-- END GENERATED:observed -->
