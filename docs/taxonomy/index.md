# Taxonomy overview

The taxonomy organises dataset changes into **five complementary dimensions**. Each change type has its own page, with its definition, its implications for ML pipelines and the adaptation it typically requires.

<!-- BEGIN GENERATED:tree -->

```mermaid
flowchart LR
    root(["Dataset changes"])
    n0["Dataset metadata"]
    root --> n0
    n1["Columns set"]
    root --> n1
    n2["Columns order"]
    n1 --> n2
    n3["Column"]
    n1 --> n3
    n4["Add column"]
    n3 --> n4
    n5["Remove column"]
    n3 --> n5
    n6["Rename column"]
    n3 --> n6
    n7["Column characteristics"]
    root --> n7
    n8["Categorical"]
    n7 --> n8
    n9["Categorical column type"]
    n8 --> n9
    n10["Categorical column values"]
    n8 --> n10
    n11["Numerical"]
    n7 --> n11
    n12["Numerical column type"]
    n11 --> n12
    n13["Numerical column values"]
    n11 --> n13
    n14["Rows set"]
    root --> n14
    n15["Rows order"]
    n14 --> n15
    n16["Row"]
    n14 --> n16
    n17["Add row"]
    n16 --> n17
    n18["Remove row"]
    n16 --> n18
    n19["Data characteristics"]
    root --> n19
    n20["Missings"]
    n19 --> n20
    n21["Correlation"]
    n19 --> n21
    n22["Data distribution"]
    n19 --> n22
```

<!-- END GENERATED:tree -->

## Index of change types

<!-- BEGIN GENERATED:index -->

| Change type | Dimension |
|---|---|
| [Dataset metadata](dataset-metadata/index.md) | [Dataset metadata](dataset-metadata/index.md) |
| [Columns order](columns-set/columns-order.md) | [Columns set](columns-set/index.md) |
| [Add column](columns-set/add-column.md) | [Columns set](columns-set/index.md) |
| [Remove column](columns-set/remove-column.md) | [Columns set](columns-set/index.md) |
| [Rename column](columns-set/rename-column.md) | [Columns set](columns-set/index.md) |
| [Categorical column type](column-characteristics/categorical-column-type.md) | [Column characteristics](column-characteristics/index.md) |
| [Categorical column values](column-characteristics/categorical-column-values.md) | [Column characteristics](column-characteristics/index.md) |
| [Numerical column type](column-characteristics/numerical-column-type.md) | [Column characteristics](column-characteristics/index.md) |
| [Numerical column values](column-characteristics/numerical-column-values.md) | [Column characteristics](column-characteristics/index.md) |
| [Rows order](rows-set/rows-order.md) | [Rows set](rows-set/index.md) |
| [Add row](rows-set/add-row.md) | [Rows set](rows-set/index.md) |
| [Remove row](rows-set/remove-row.md) | [Rows set](rows-set/index.md) |
| [Missings](data-characteristics/missings.md) | [Data characteristics](data-characteristics/index.md) |
| [Correlation](data-characteristics/correlation.md) | [Data characteristics](data-characteristics/index.md) |
| [Data distribution](data-characteristics/data-distribution.md) | [Data characteristics](data-characteristics/index.md) |

<!-- END GENERATED:index -->

## How each page is organised

- **Dimension pages** define the dimension and list the change types it contains.
- **Change type pages** describe *what changes*, the *implications for the pipeline*, the *typical adaptation* and where the change was *observed in practice*.
