# Numerical column format

The way numbers are written changes, while their value stays the same. Examples:

- the **decimal separator** (dot or comma),
- **standard vs. scientific notation**,
- the **encoding format** of the numerical values.

## Pipeline implication examples

The underlying semantics of the data are not affected, but the values may no longer be parsed correctly (for instance, a comma as decimal separator read as a field separator or as text).

## Typical adaptation

Data ingestion or parsing components of the pipeline.

!!! note "Not to be confused with"
    [Format](../../../storage/format.md) in the Storage dimension, which concerns the file format and the field delimiter, not how each number is written.

See also: [Numerical column values](numerical-column-values.md).
