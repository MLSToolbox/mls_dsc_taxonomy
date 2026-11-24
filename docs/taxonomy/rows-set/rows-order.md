# Rows order

*Dimension: [Rows set](index.md)*

## What changes

The rows appear in a different sequence, while the set of rows stays the same.

## Pipeline implications

Affects pipelines that rely on **positional access** to data, for instance fixed index-based splits.

## Typical adaptation

Data ingestion or preprocessing components.

See also: [Columns order](../columns-set/columns-order.md).
