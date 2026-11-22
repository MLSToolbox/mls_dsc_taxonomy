# Column Order (C210)

**Perspective:** [Column Set](../perspectives/column-set.md)

## Description

Changes in the order of columns in a dataset.

## Examples

Two versions may contain the same columns but arrange them in a different sequence.

## Potential implications for ML pipeline evolution

For pipelines that access columns by position, changes in column order may lead to incorrect feature selection or execution failures, requiring adaptations in data ingestion or preprocessing components. Pipelines that access columns by name are less directly affected by column order.
