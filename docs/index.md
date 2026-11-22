# Taxonomy of Dataset Changes for ML Pipeline Evolution

A catalogue of the **changes that tabular datasets undergo across versions** and of their **potential implications for the evolution of Machine Learning (ML) pipelines** that reuse them.

As ML repositories such as Hugging Face grow, datasets are republished, forked and modified. Those changes can silently alter the behaviour, quality and maintainability of the pipelines built on top of them. This site makes the taxonomy browsable, with **its own page and URL for every change type** (e.g. *Rename column*).

<div class="grid cards" markdown>

- :lucide-network: **[Explore the taxonomy](taxonomy/index.md)**

    Five dimensions, fifteen elementary change types.

- :lucide-clipboard-check: **[See the validation](validation/census-income.md)**

    Changes found across nine versions of the Census Income dataset.

- :lucide-quote: **[How to cite](about.md#how-to-cite)**

    Reference the paper and this website.

</div>

## At a glance

| Dimension | Typical question it answers |
|---|---|
| [Dataset metadata](taxonomy/dataset-metadata/index.md) | Can I still use and load this dataset as it was published? |
| [Columns set](taxonomy/columns-set/index.md) | Which columns exist, in what order, with what names? |
| [Column characteristics](taxonomy/column-characteristics/index.md) | What type and values does each column hold? |
| [Rows set](taxonomy/rows-set/index.md) | Which instances are included, and in what order? |
| [Data characteristics](taxonomy/data-characteristics/index.md) | How does the data behave: missings, correlations, distributions? |

!!! note "Scope"
    The taxonomy describes **intrinsic properties of the dataset**, not how a particular pipeline uses it. Whether a column is the target or an input feature depends on the pipeline, so it is not a dataset change. It lists **elementary** changes; several can occur at once.

## Machine-readable data

The taxonomy and the validation table are available as YAML for reuse:
[`data/taxonomy.yaml`](https://github.com/GITHUB_USER/dataset-changes-taxonomy/blob/main/data/taxonomy.yaml) and
[`data/census-income-versions.yaml`](https://github.com/GITHUB_USER/dataset-changes-taxonomy/blob/main/data/census-income-versions.yaml).
