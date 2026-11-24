# Horizontal

## What changes

The rows of the dataset are physically divided into subsets, or divided differently from the reference version: for example, one file in one version and several files or partitions in another.

## Pipeline implications

A pipeline that reads a single file or path may silently load only part of the data. Loading several parts requires listing them and putting them together.

## Typical adaptation

Data loading components: enumerate the parts, concatenate them and check that their structure is consistent; update path patterns or configuration.

See also: [Vertical](vertical.md), [Extra row](../../instances/rows-set/row/extra-row.md).
