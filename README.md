# 减五度 诗 (Poems by Quinta Diminuita)

This is a static site for the poetry collection "减五度 诗".

## Build

The site is built using a custom Python script.

```bash
python3 scripts/build.py
```

The output is in `docs/` (configured for GitHub Pages).

## Serve

To preview the site:

```bash
cd docs
python3 -m http.server
```

Then open http://localhost:8000.

## Source

- `whole-text`: The source text file containing all poems.
- `scripts/parse_poems.py`: Logic to parse the text file.
- `scripts/build.py`: Logic to generate the HTML site.
- `assets/`: CSS and images.
- `_layouts/`: HTML template.
