# Add Row (C421)

**Perspective:** [Row Set](../perspectives/row-set.md)

## Description

The addition of one or more rows (instances) to a dataset.

## Examples

New observations, outliers, or duplicate instances may be added.

## Potential implications for ML pipeline evolution

The potential impact depends on the characteristics of the affected rows. Adding outliers may alter the data distribution and influence model training or evaluation. Adding duplicate instances may affect the relative frequency of examples without introducing new information. These changes may require adaptations in data preparation procedures, sampling strategies, model retraining, or evaluation processes.
