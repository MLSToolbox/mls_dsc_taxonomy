# Taxonomy of Dataset Changes for ML Pipeline Evolution

Source of the website for the paper:
Alberto Abelló, Cristina Gómez, Lidia López, and Claudia Ayala. “A Taxonomy of Dataset Changes for Supporting Machine Learning Pipeline Evolution.” PROFES 2026, Lecture Notes in Computer Science, vol. 17339, 2027. https://doi.org/10.1007/978-3-032-45954-1_32

The taxonomy comprises five dimensions and fifteen elementary change categories. 

Built with [Zensical](https://zensical.org) and deployed to GitHub Pages.

## Structure

```
docs/
  index.md, about.md
  taxonomy/
    index.md                     Overview, tree diagram, index (generated)
    <dimension>/index.md         One folder per dimension
    <dimension>/<change-type>.md One page per change type
  validation/census-income.md    Validation with nine dataset versions
data/taxonomy.yaml               The taxonomy as structured data
data/census-income-versions.yaml Table 1 of the paper as structured data
scripts/taxonomy.py              check / generate
zensical.toml                    Site configuration and navigation
.github/workflows/docs.yml       Build and deploy to GitHub Pages
```

Change types and dimensions are identified **by name (slug), not by numeric codes**, because the taxonomy may evolve. Names and file paths can be changed freely.

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

**Add a change type**

1. Add it to `data/taxonomy.yaml` (key, name, page).
2. Create the page by copying an existing one from the same dimension. Keep the `observed` generated block at the end.
3. Add the page to `nav` in `zensical.toml`.
4. Run `python scripts/taxonomy.py check` and then `generate`.

**Rename or move a change type**: change `name`/`page` in the YAML, rename the file, update `nav` and the relative links to it (the build warns about broken links), and run `generate`. Add the new key to `changes` in `data/census-income-versions.yaml` if it was already used there.

**Add a dataset version**: add an entry in `data/census-income-versions.yaml` and run `generate`. If the number of change types per version no longer matches the paper, update `REPORTED_TOTALS` in `scripts/taxonomy.py`.

Everything between `<!-- BEGIN GENERATED:... -->` and `<!-- END GENERATED:... -->` is rewritten by `generate`; do not edit it by hand.
