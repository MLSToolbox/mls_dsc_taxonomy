# Columns order

*Dimension: [Columns set](index.md)*

## What changes

The columns appear in a different sequence, while the set of columns and their content stay the same.

## Pipeline implications

Pipelines that access columns **by position** may select the wrong features or fail. Pipelines that access columns by name are unaffected.

## Typical adaptation

Data ingestion or preprocessing components: select columns by name, or realign them to the expected order.

See also: [Rename column](rename-column.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **3 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D3, D4, D8.

<!-- END GENERATED:observed -->
