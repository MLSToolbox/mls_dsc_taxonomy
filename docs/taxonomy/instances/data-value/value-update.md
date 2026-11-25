# Value update not involving missing

A non-missing value takes the place of another non-missing value. It concerns modifications of individual values, such as corrections or perturbations. A systematic transformation of a whole column is described in [Numerical column values](../../schema/column-characteristics/numerical/numerical-column-values.md).

## Pipeline implication examples

Modifies the data on which models are trained or evaluated, which may influence model performance and alter the distributions of, and the correlations among, features.

The impact also depends on the role of the affected attribute in the ML task. When the updated values belong to the **target variable**, the change may correspond to **concept drift** (the relationship between the input features and the target changes) and may alter the class distribution, a situation known as **class imbalance**.

## Typical adaptation

Data preprocessing adjustments, model retraining or recalibration of evaluation procedures; resampling or class weighting for class imbalance.
