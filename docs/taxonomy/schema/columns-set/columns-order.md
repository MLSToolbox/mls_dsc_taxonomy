# Columns order

The columns appear in a different sequence, while the set of columns and their content stay the same.

## Pipeline implication examples

Pipelines that access columns **by position** may select the wrong features or fail. Pipelines that access columns by name are unaffected.

## Typical adaptation

Data ingestion or preprocessing components: select columns by name, or realign them to the expected order.

See also: [Rename column](column/rename-column.md).
