# Column characteristics

Differences affecting the characteristics of **individual columns without modifying the set of columns** in the dataset. Categorical and numerical columns are distinguished because differences in each may have different implications for ML pipeline evolution. In both cases the **type** of the column or the **values** it holds can change, and numerical columns can also change their **format**.

!!! info "A note on ordering"
    Numerical columns are inherently ordered, whereas categorical columns may or may not have an associated order. Differences in the ordering of categorical values are **not** covered here, since that information is typically provided externally (domain knowledge or metadata) rather than contained in the data; see [Metadata](../../metadata.md).

## Difference types

<!-- BEGIN GENERATED:types -->

- **Categorical**
    - [Categorical column type](categorical/categorical-column-type.md)
    - [Categorical column values](categorical/categorical-column-values.md)
- **Numerical**
    - [Numerical column type](numerical/numerical-column-type.md)
    - [Numerical column values](numerical/numerical-column-values.md)
    - [Numerical column format](numerical/numerical-column-format.md)

<!-- END GENERATED:types -->
