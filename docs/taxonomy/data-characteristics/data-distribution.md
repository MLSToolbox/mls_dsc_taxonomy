# Data distribution

*Dimension: [Data characteristics](index.md)*

## What changes

The distribution of the data changes. It may be a consequence of [adding](../rows-set/add-row.md) or [removing](../rows-set/remove-row.md) rows, or of other modifications.

## Pipeline implications

Modifies the characteristics of the data on which models are trained or evaluated, influencing model performance. When it affects the target variable, it may correspond to **concept drift** or **class imbalance** (see the [dimension page](index.md)).

## Typical adaptation

Data preprocessing adjustments, model retraining or recalibration of evaluation procedures; resampling or class weighting for class imbalance.

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **2 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D6, D9.

<!-- END GENERATED:observed -->
