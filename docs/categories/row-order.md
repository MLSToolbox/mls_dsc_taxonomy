# Row Order (C410)

**Perspective:** [Row Set](../perspectives/row-set.md)

## Description

Changes in the ordering of rows in a dataset.

## Examples

The same instances may appear in a different sequence in two dataset versions.

## Potential implications for ML pipeline evolution

Changes to row ordering may affect ML pipelines that rely on positional access to data, potentially requiring adaptations in data ingestion or preprocessing components.
