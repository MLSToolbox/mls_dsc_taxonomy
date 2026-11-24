# Taxonomy of Dataset Differences for ML Pipeline Evolution

Source of the website for the paper:
Alberto Abelló, Cristina Gómez, Lidia López, and Claudia Ayala. “A Taxonomy of Dataset Changes for Supporting Machine Learning Pipeline Evolution.” PROFES 2026, Lecture Notes in Computer Science, vol. 17339, 2027. https://doi.org/10.1007/978-3-032-45954-1_32

The taxonomy comprises five dimensions and fifteen elementary change categories. 

Built with [Zensical](https://zensical.org) and deployed to GitHub Pages.

## Structure

```
docs/
  index.md, about.md
  taxonomy/
    index.md                      Overview, tree diagram and index (generated)
    <dimension>/index.md          Metadata, Schema, Instances, Storage
    <dimension>/<category>/index.md
    <dimension>/<category>/[<group>/]<change-type>.md
data/taxonomy.yaml                The taxonomy as structured data (source of truth)
templates/change-type.md          Template for a new change type page
scripts/taxonomy.py               generate / check
zensical.toml                     Site configuration (the menu is generated)
.github/workflows/docs.yml        Build and deploy to GitHub Pages
```

Dimensions, categories, and difference types are identified **by name (slug), not by numeric codes**, because the taxonomy may evolve. Names and file paths can be changed freely.

## Local preview

```bash
pip install -r requirements.txt
python scripts/taxonomy.py generate
zensical serve          # http://localhost:8000
```

## Publishing

1. Replace every `GITHUB_USER` with your user/organisation (`zensical.toml`, `CITATION.cff`, `docs/`).
2. Push to the `main` branch.
3. In the repository go to **Settings → Pages → Build and deployment → Source** and choose **GitHub Actions**.
4. The workflow publishes the site at `https://GITHUB_USER.github.io/dataset-changes-taxonomy/`.

## Evolving the taxonomy

The tree diagram, the index, the lists of contents and the **menu** are generated from `data/taxonomy.yaml`. Never edit them by hand: every Markdown page contains `<!-- BEGIN GENERATED:... -->` blocks, and `zensical.toml` contains `# BEGIN GENERATED:nav`.

**Add a difference type**

1. Add it to `data/taxonomy.yaml` (key, name, page).
2. Create the page by copying `templates/change-type.md` to the path given in `page`.
3. Run `python scripts/taxonomy.py generate` and then `python scripts/taxonomy.py check`.

**Add a category or a dimension**: same steps, using the template of a similar page (those with a *Difference types* / *Categories and difference types* section include the `types` block).

**Add a grouping level without a page** (like *Column* or *Categorical*): add a node without `page` in the YAML and put the files of its children in a folder with its name.

**Rename or move a difference category**: change `name`/`page` in the YAML, move the file and run `generate`. Relative links written by hand in the text (the *See also* lines) are not updated; the build warns about broken links.

**Hide a grouping node from the menu**: `nav: false` in the YAML (used for *Dataset*).

Everything between `<!-- BEGIN GENERATED:... -->` and `<!-- END GENERATED:... -->` is rewritten by `generate`; do not edit it by hand.
