# Remove Column (C222)

**Perspective:** [Column Set](../perspectives/column-set.md)

## Description

The removal of one or more columns from a dataset.

## Examples

An attribute present in one version may be absent from a subsequent version.

## Potential implications for ML pipeline evolution

Removing columns may cause failures if the removed columns are explicitly required by the pipeline, entailing modifications to feature engineering steps, model inputs, or retraining procedures.
