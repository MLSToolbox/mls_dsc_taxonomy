# Columns set

*Dimension of the taxonomy*

Changes affecting **the set of columns** that constitute a dataset. Their impact depends on **how the ML pipeline references columns**: by position or by name.

!!! tip "Positional vs. by-name access"
    Changing the order of columns mainly hurts pipelines that access columns by position, whereas renaming a column mainly hurts pipelines that access them by name. Knowing which access style your pipeline uses tells you which one to worry about.

## Change types

<!-- BEGIN GENERATED:types -->

- [Columns order](columns-order.md)
- **Column**
    - [Add column](column/add-column.md)
    - [Remove column](column/remove-column.md)
    - [Rename column](column/rename-column.md)

<!-- END GENERATED:types -->
