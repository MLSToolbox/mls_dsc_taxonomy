# Numerical column values

## What changes

The values of a numerical column are transformed in scale or distribution: multiplicative factors, logarithmic transformations, normalisation techniques (min-max scaling, standardisation) or value perturbation for obfuscation purposes.

A systematic transformation of the values of a whole column belongs here; modifications of individual values are described in [Value update not involving missing](../../../instances/data-value/value-update.md).

## Pipeline implications

Scale and distribution changes affect feature scaling and model behaviour. Representation changes may leave the underlying semantics intact but can still break parsing.

## Typical adaptation

Preprocessing steps, feature scaling procedures or model retraining.

See also: [Numerical column format](numerical-column-format.md), [Categorical column values](../categorical/categorical-column-values.md).
