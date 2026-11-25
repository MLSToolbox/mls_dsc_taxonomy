# Extra column

The dataset contains a column that is not present in the reference version. Extra columns may contain completely new data or just data derived from existing ones.

## Pipeline implication examples

Modifies the input data available to the pipeline. Automatic feature selection mechanisms may be affected by the new attribute.

## Typical adaptation

Incorporate the new attribute into the pipeline when it is relevant, or adjust feature selection steps so that it is handled (or deliberately ignored).

See also: [Absent column](absent-column.md).
