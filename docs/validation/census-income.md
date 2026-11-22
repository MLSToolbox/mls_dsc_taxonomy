# Validation: Census Income dataset

As a preliminary assessment, we analysed nine public versions of the **[Census Income (Adult)](https://archive.ics.uci.edu/dataset/2/adult)** dataset, each one an evolution of the original. The dataset has 14 attributes (age, race, occupation, education, among others) and a binary label indicating whether annual income exceeds $50K.

The objective was to check whether the taxonomy is **comprehensive enough to characterise the changes observed in practice**.

## Versions analysed

<!-- BEGIN GENERATED:versions -->

| ID | Version |
|---|---|
| D1 | [scikit-learn/adult-census-income](https://huggingface.co/datasets/scikit-learn/adult-census-income) |
| D2 | [AiresPucrs/adult-census-income](https://huggingface.co/datasets/AiresPucrs/adult-census-income) |
| D3 | [mstz/adult (income)](https://huggingface.co/datasets/mstz/adult/tree/main/income) |
| D4 | [mstz/adult (income-no race)](https://huggingface.co/datasets/mstz/adult/tree/main/income-no%20race) |
| D5 | [databoost/optimized_adult_census](https://huggingface.co/datasets/databoost/optimized_adult_census) |
| D6 | [ETdanR/adult_income](https://huggingface.co/datasets/ETdanR/adult_income) |
| D7 | [kuldeepbishnoi29/adult-fairness](https://huggingface.co/datasets/kuldeepbishnoi29/adult-fairness) |
| D8 | [Zenodo record 12533514](https://zenodo.org/records/12533514) |
| D9 | [AIF360 AdultDataset (v0.5.0)](https://aif360.readthedocs.io/en/v0.5.0/modules/generated/aif360.datasets.AdultDataset.html) |

<!-- END GENERATED:versions -->

## Change types per version

Rows are the change types of the [taxonomy](../taxonomy/index.md), columns are the dataset versions.

<!-- BEGIN GENERATED:matrix -->

| Change type | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| [Dataset metadata](../taxonomy/dataset-metadata/index.md) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | 9 |
| [Columns order](../taxonomy/columns-set/columns-order.md) |  |  | ✔ | ✔ |  |  |  | ✔ |  | 3 |
| [Add column](../taxonomy/columns-set/add-column.md) |  |  |  |  | ✔ |  |  | ✔ |  | 2 |
| [Remove column](../taxonomy/columns-set/remove-column.md) |  |  |  | ✔ |  |  | ✔ | ✔ | ✔ | 4 |
| [Rename column](../taxonomy/columns-set/rename-column.md) | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  | 8 |
| [Categorical column type](../taxonomy/column-characteristics/categorical-column-type.md) |  |  | ✔ | ✔ |  |  |  |  |  | 2 |
| [Categorical column values](../taxonomy/column-characteristics/categorical-column-values.md) |  |  | ✔ | ✔ |  |  | ✔ | ✔ | ✔ | 5 |
| [Numerical column type](../taxonomy/column-characteristics/numerical-column-type.md) |  |  |  |  |  |  |  | ✔ |  | 1 |
| [Numerical column values](../taxonomy/column-characteristics/numerical-column-values.md) |  |  |  |  |  |  |  | ✔ |  | 1 |
| [Rows order](../taxonomy/rows-set/rows-order.md) | ✔ | ✔ | ✔ |  | ✔ |  |  |  |  | 4 |
| [Add row](../taxonomy/rows-set/add-row.md) |  |  |  |  |  |  | ✔ |  |  | 1 |
| [Remove row](../taxonomy/rows-set/remove-row.md) |  |  | ✔ | ✔ |  | ✔ |  | ✔ |  | 4 |
| [Missings](../taxonomy/data-characteristics/missings.md) |  |  |  |  |  |  |  |  | ✔ | 1 |
| [Correlation](../taxonomy/data-characteristics/correlation.md) |  |  |  |  |  |  |  |  | ✔ | 1 |
| [Data distribution](../taxonomy/data-characteristics/data-distribution.md) |  |  |  |  |  | ✔ |  |  | ✔ | 2 |
| **Total** | **3** | **3** | **7** | **7** | **4** | **4** | **5** | **9** | **6** | |

<!-- END GENERATED:matrix -->

## Main findings

- **All observed modifications could be mapped** to a change type of the taxonomy.
- Dataset metadata changes appear in **every** version; renaming columns in all but one.
- Changes to numerical columns are the least frequent, reflecting the predominantly categorical nature of the dataset.
- Evolution ranges from **3 change types** (D1, D2) to **9 of the 15** (D8).
- Datasets often undergo **several simultaneous changes**, which may require coordinated adaptations across pipeline components.

## Method

Changes were identified by combining repository information (e.g. dataset cards, when available) with manual inspection of the data. Two researchers inspected the datasets independently and resolved disagreements through discussion. Documentation revealed explicitly reported modifications; manual analysis revealed additional undocumented ones.

!!! warning "Limitations"
    The assessment covers a single dataset and versions from public repositories (mainly Hugging Face). Further evaluation across more datasets, domains and an expert review is planned.
