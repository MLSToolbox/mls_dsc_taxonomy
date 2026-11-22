# Data characteristics

*Dimension of the taxonomy*

Changes in the **intrinsic characteristics of the data**: value distributions, relationships among variables and semantic properties.

Some of these changes may result from adding or removing rows, but they are kept separate: **[rows set](../rows-set/index.md) changes concern *which* instances are included, whereas data characteristic changes concern *how the data behaves* and the patterns it represents.**

The impact also depends on the **role of the affected attributes** in the ML task:

- If the change affects the **target variable**, it may correspond to **concept drift**: the relationship between input features and the target changes over time.
- If it modifies the **distribution of target values in a classification problem**, it is commonly referred to as **class imbalance**, requiring adaptation strategies such as resampling, class weighting or model retraining.

## Change types

<!-- BEGIN GENERATED:types -->

- [Missings](missings.md)
- [Correlation](correlation.md)
- [Data distribution](data-distribution.md)

<!-- END GENERATED:types -->
