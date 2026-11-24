# Remove row

## What changes

Instances that are present in the reference version are not present in this one.

## Pipeline implications

Modifies the instances available for training, validation or testing. The absence of a unique and representative instance may reduce coverage of relevant patterns; absent outliers or duplicates affect the distribution or the relative frequencies (see the [table of affected rows](../index.md)).

## Typical adaptation

Data preparation procedures, sampling strategies, model retraining or evaluation processes.

See also: [Extra row](extra-row.md), [Horizontal fragmentation](../../../storage/fragmentation/horizontal.md).
