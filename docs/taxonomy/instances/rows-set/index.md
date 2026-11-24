# Rows set

Changes affecting **the set of rows** that constitute a dataset.

Extra or absent rows modify the instances available for training, validation or testing, but **the impact depends on the characteristics of the affected rows**:

!!! note "Detecting the differences"
    Deciding with certainty whether rows are extra or absent is hard without an identifier. The taxonomy only classifies the differences, not the mechanism used to detect them.

| Affected rows | Effect |
|---|---|
| Outliers | May alter the data distribution and influence model training or evaluation. |
| A unique and representative instance | Its absence may reduce the coverage of relevant patterns in the data. |
| Duplicates | Changes the relative frequency of examples without introducing new information. |

## Difference types

<!-- BEGIN GENERATED:types -->

- [Rows order](rows-order.md)
- **Row**
    - [Extra row](row/extra-row.md)
    - [Absent row](row/absent-row.md)

<!-- END GENERATED:types -->
