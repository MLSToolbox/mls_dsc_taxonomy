# Absent column

A column that is present in the reference version is not present in this one.

## Pipeline implication examples

The pipeline fails if the absent column is **explicitly required**, for example as a feature, as the target, or in a preprocessing step.

## Typical adaptation

Modify feature engineering steps, model inputs or retraining procedures, or replace the dataset if the column is essential.

See also: [Extra column](extra-column.md).
