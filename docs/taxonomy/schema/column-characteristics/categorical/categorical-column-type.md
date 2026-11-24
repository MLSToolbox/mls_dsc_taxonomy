# Categorical column type

## What changes

The data type of a categorical column changes. Examples: encoding categorical variables as booleans through one-hot encoding, or transforming numerical columns into categorical ones and vice versa.

## Pipeline implications

Different ML algorithms and pipeline components rely on specific data representations, so a new representation may not be accepted or may be interpreted differently.

## Typical adaptation

Data preprocessing, feature engineering and model configuration.

See also: [Numerical column type](../numerical/numerical-column-type.md).
