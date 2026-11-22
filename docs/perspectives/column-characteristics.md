# Column Characteristics

**Identifier:** C300

This perspective addresses changes affecting the characteristics of individual columns without modifying the set of columns in the dataset. It distinguishes between categorical and numerical columns, as changes in each type may have different implications for ML pipeline evolution.

Numerical columns are inherently ordered, whereas categorical columns may or may not have an associated order. Changes in the ordering of categorical values are not included in the taxonomy because such information is typically not contained in the dataset itself, but is provided externally through domain knowledge or metadata.

## Elementary categories

- [Categorical Column Type (C311)](../categories/categorical-column-type.md)
- [Categorical Column Values (C312)](../categories/categorical-column-values.md)
- [Numerical Column Type (C321)](../categories/numerical-column-type.md)
- [Numerical Column Values (C322)](../categories/numerical-column-values.md)
