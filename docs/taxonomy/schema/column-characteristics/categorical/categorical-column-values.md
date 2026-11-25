# Categorical column values

The set of values represented in a categorical column changes: categories are **added or removed**, or **mappings are applied**, for instance to anonymise existing values.

## Pipeline implication examples

Encoders trained on the previous categories may fail or silently mis-encode unseen or missing values.

## Typical adaptation

Update encoding strategies, validation rules or model inputs.

See also: [Numerical column values](../numerical/numerical-column-values.md).
