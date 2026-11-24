# Format

## What changes

The **file format** in which the data are distributed changes (for example, from CSV to Parquet), or the **field delimiter** of a delimited file changes (for example, from comma to semicolon), while the data themselves stay the same.

## Pipeline implications

Can directly affect pipeline execution: ingestion or preprocessing steps may fail or may parse the data incorrectly.

## Typical adaptation

Modify the data loading and preprocessing components (reader, delimiter and parsing settings).

!!! example "Example"
    A new version of a dataset is published as Parquet instead of CSV. The loader fails before any model code runs, so the fix lives entirely in the **ingestion** step.

See also: [Numerical column format](../schema/column-characteristics/numerical/numerical-column-format.md), [Fragmentation](fragmentation/index.md).
