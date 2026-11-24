# Vertical

## What changes

The columns of the dataset are physically divided into subsets, or divided differently from the reference version: for example, the features in one file and the target in another.

## Pipeline implications

The parts have to be joined to rebuild the dataset. If rows cannot be aligned reliably (no common key, different order), features and target may be mismatched.

## Typical adaptation

Data loading components: add a join step, define the key and check the alignment of the rows.

See also: [Horizontal](horizontal.md), [Extra column](../../schema/columns-set/column/extra-column.md).