# Rows set

*Dimension of the taxonomy*

Changes affecting **the set of rows** that constitute a dataset.

Adding or removing rows modifies the instances available for training, validation or testing, but **the impact depends on the characteristics of the affected rows**:

| Affected rows | Effect |
|---|---|
| Outliers | May alter the data distribution and influence model training or evaluation. |
| A unique and representative instance | Removing it may reduce the coverage of relevant patterns in the data. |
| Duplicates | Changes the relative frequency of examples without introducing new information. |

## Change types

<!-- BEGIN GENERATED:types -->

- [Rows order](rows-order.md)
- **Row**
  - [Add row](add-row.md)
  - [Remove row](remove-row.md)

<!-- END GENERATED:types -->
