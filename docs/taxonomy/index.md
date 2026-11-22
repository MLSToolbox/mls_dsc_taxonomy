# Taxonomy of Dataset Changes

The taxonomy characterizes dataset changes that may affect ML pipeline evolution from five complementary perspectives. Each type of change is assigned a unique identifier to facilitate reference.

The taxonomy describes intrinsic dataset properties rather than their use within a specific ML pipeline. For example, whether a column is used as a target or an input feature depends on the pipeline design, not on the dataset itself. It focuses on elementary changes, although multiple change types may occur simultaneously (e.g., changes in missing values often coincide with changes in data distribution).

Each category is accompanied by examples illustrating its potential implications for ML pipeline evolution.

## Perspectives and categories

- [Metadata](perspectives/metadata.md): [Metadata (C100)](categories/metadata.md).
- [Column Set (C200)](perspectives/column-set.md): [Column Order (C210)](categories/column-order.md), [Add Column (C221)](categories/add-column.md), [Remove Column (C222)](categories/remove-column.md), [Rename Column (C223)](categories/rename-column.md).
- [Column Characteristics (C300)](perspectives/column-characteristics.md): [Categorical Column Type (C311)](categories/categorical-column-type.md), [Categorical Column Values (C312)](categories/categorical-column-values.md), [Numerical Column Type (C321)](categories/numerical-column-type.md), [Numerical Column Values (C322)](categories/numerical-column-values.md).
- [Row Set (C400)](perspectives/row-set.md): [Row Order (C410)](categories/row-order.md), [Add Row (C421)](categories/add-row.md), [Remove Row (C422)](categories/remove-row.md).
- [Data Characteristics (C500)](perspectives/data-characteristics.md): [Missing Values (C510)](categories/missing-values.md), [Correlation (C520)](categories/correlation.md), [Data Distribution (C530)](categories/data-distribution.md).
