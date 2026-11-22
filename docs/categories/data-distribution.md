# Data Distribution (C530)

**Perspective:** [Data Characteristics](../perspectives/data-characteristics.md)

## Description

Changes in the distributions of values in a dataset.

## Examples

The distribution of values may change across dataset versions. When changes affect the target variable, they may correspond to concept drift, where the relationship between input features and the target changes over time. Changes to the distribution of target values in classification problems are commonly referred to as class imbalance.

## Potential implications for ML pipeline evolution

Changes in data distributions may influence model performance by modifying the characteristics of the data on which models are trained or evaluated. They may require data-preprocessing adjustments, model retraining, or recalibration of evaluation procedures. When changes affect the target, concept drift may be involved; changes in target-value distributions in classification may require adaptation strategies such as resampling, class weighting, or model retraining.
