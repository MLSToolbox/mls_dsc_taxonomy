# Rename Column (C223)

**Perspective:** [Column Set](../perspectives/column-set.md)

## Description

Changes to the names of columns in a dataset.

## Examples

A column name may change while the corresponding attribute remains part of the dataset.

## Potential implications for ML pipeline evolution

For pipelines that access columns by name, column renaming may invalidate feature references and require updates to the corresponding data-processing or feature-engineering steps.
