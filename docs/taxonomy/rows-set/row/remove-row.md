# Remove row

*Dimension: [Rows set](../index.md)*

## What changes

Instances are removed from the dataset.

## Pipeline implications

Modifies the instances available for training, validation or testing. Removing a unique and representative instance may reduce coverage of relevant patterns; removing outliers or duplicates affects distribution or relative frequencies (see the [table of affected rows](index.md)).

## Typical adaptation

Data preparation procedures, sampling strategies, model retraining or evaluation processes.

See also: [Add row](add-row.md), [Data distribution](../data-characteristics/data-distribution.md).

## Observed in practice

<!-- BEGIN GENERATED:observed -->

Observed in **4 of 9** analysed versions of the [Census Income dataset](../../validation/census-income.md): D3, D4, D6, D8.

<!-- END GENERATED:observed -->
