# Column characteristics

*Dimension of the taxonomy*

Changes affecting the characteristics of **individual columns without modifying the set of columns** in the dataset. Categorical and numerical columns are distinguished because changes in each may have different implications for ML pipeline evolution. In both cases a change can affect the **type** of the column or the **values** it holds.

!!! info "A note on ordering"
    Numerical columns are inherently ordered, whereas categorical columns may or may not have an associated order. Changes in the ordering of categorical values are **not** included in the taxonomy, since that information is typically provided externally (domain knowledge or metadata) rather than contained in the dataset.

## Change types

<!-- BEGIN GENERATED:types -->

- **Categorical**
    - [Categorical column type](categorical-column-type.md)
    - [Categorical column values](categorical-column-values.md)
- **Numerical**
    - [Numerical column type](numerical-column-type.md)
    - [Numerical column values](numerical-column-values.md)

<!-- END GENERATED:types -->
