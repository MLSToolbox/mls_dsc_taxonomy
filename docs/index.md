# Taxonomy of Dataset Differences for ML Pipeline Evolution

A catalogue of the **differences that tabular datasets undergo across versions** and of their **potential implications for the evolution of Machine Learning (ML) pipelines** that reuse them.

As ML repositories such as Hugging Face grow, datasets are republished, forked and modified. Those differences can silently alter the behaviour, quality and maintainability of the pipelines built on top of them. This site makes the taxonomy browsable, with **its own page and URL for every change type** (e.g. *Rename column*).

<div class="grid cards" markdown>

- :lucide-network: **[Explore the taxonomy](taxonomy/index.md)**

    Four dimensions (Metadata, Schema, Instances, Storage) and nineteen change types.

- :lucide-quote: **[How to cite](about.md#how-to-cite)**

    Reference the paper and this website.
</div>

## At a glance

| Part of the taxonomy | Typical question it answers |
|---|---|
| [Metadata](taxonomy/metadata/index.md) | Can I still use this dataset (license, source, language, split…)? |
| [Schema](taxonomy/schema/index.md) | Which columns exist, and what type, values and format do they have? |
| [Instances](taxonomy/instances/index.md) | Which rows are included, and which values do they hold? |
| [Storage](taxonomy/storage/index.md) | In which format are the data stored, and how are they split into files? |

!!! note "Scope"
    The taxonomy describes **intrinsic properties of the dataset**, not how a particular pipeline uses it. Whether a column is the target or an input feature depends on the pipeline, so it is not a dataset change. It lists **elementary** changes; several can occur at once.

## Machine-readable data

The taxonomy is available as YAML for reuse: [`data/taxonomy.yaml`](https://github.com/GITHUB_USER/dataset-changes-taxonomy/blob/main/data/taxonomy.yaml).
