# Remove Row (C422)

**Perspective:** [Row Set](../perspectives/row-set.md)

## Description

The removal of one or more rows (instances) from a dataset.

## Examples

Rows may be removed that correspond to outliers, unique and representative instances, or duplicate instances.

## Potential implications for ML pipeline evolution

The potential impact depends on the characteristics of the affected rows. Removing outliers may alter the data distribution. Removing a unique and representative instance may reduce the coverage of relevant patterns, whereas removing duplicates may affect the relative frequency of examples without introducing new information. These changes may require adaptations in data preparation procedures, sampling strategies, model retraining, or evaluation processes.
