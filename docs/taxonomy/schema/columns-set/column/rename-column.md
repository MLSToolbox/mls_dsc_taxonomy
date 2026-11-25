# Rename column

A column keeps its content but changes its name.

## Pipeline implication examples

Pipelines that access columns **by name** see their feature references invalidated, even though the data itself is the same. Position-based pipelines are unaffected.

## Typical adaptation

Update the corresponding data processing or feature engineering steps, typically through a mapping from old to new names.

See also: [Columns order](../columns-order.md).
