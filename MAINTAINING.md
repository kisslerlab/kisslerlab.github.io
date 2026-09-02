# Maintaining the Kissler Lab site

A practical guide to keeping this site up to date — written for Stephen and for
future Claude sessions. The site is a **custom Jekyll theme** (no external theme);
content lives in Markdown and `_data/*.yml`, and the design lives in `_layouts`,
`_includes`, and `assets/css/main.scss`.

## Run it locally

```bash
bundle install          # first time only
bundle exec jekyll serve # then open http://localhost:4000
```

Edits to `.md`, `_data`, `_includes`, and `_layouts` hot-reload. Editing
`_config.yml` requires restarting the server.

## Deploying

The live site builds from the **`master`** branch on GitHub Pages. This redesign
lives on the **`redesign`** branch — merge it to `master` (or push to `master`)
to publish. There's no build step to run; GitHub Pages builds Jekyll for you.

---

## Common edits

### Add or update a publication  → `_data/publications.yml`

Each entry looks like:

```yaml
  - title: "Paper title"
    authors: "First Author, …, Stephen M. Kissler"   # order matters
    venue: "Journal or medRxiv/arXiv"
    year: 2026
    type: paper            # or: preprint
    tags: [viral-kinetics, surveillance]   # options are the `filters:` at the top
    senior: true           # true if Stephen is FIRST, LAST, or co-senior author
    url: "https://doi.org/…"
```

Keep the list **newest first**. Notes:

- **`senior`** is the important flag: the home page's "Recent work" strip shows
  the **six most recent `senior: true`** papers. Set it `true` only when Stephen
  is first, last, or co-senior (e.g. the measles paper, where he's second-to-last
  but co-senior). Middle-author papers get `senior: false` (or omit it).
- **`tags`** drive the topic filter chips on `/research/`. To add a new topic,
  add it under `filters:` at the top of the file, then tag papers with it.
- **`authors`** — verify against the DOI. Author lists are easy to get wrong from
  memory; the reliable source is Crossref:
  `curl "https://api.crossref.org/works/<DOI>"`. Use `…` to elide a long list
  (e.g. `"First Author, …, Stephen M. Kissler"`).
- Lab members' names are **bolded automatically** — see below.

### Bold a new lab member in author lists  → `_data/lab_names.yml`

Any name in `_data/lab_names.yml` is wrapped in **bold** wherever it appears in a
publication's author string (via `_includes/authors.html`). When someone joins,
add every form their name might take, e.g.:

```yaml
- "Jane Q. Public"
- "Jane Public"
```

### Add or update a person  → `_data/people.yml` (+ a bio page)

- `_data/people.yml` has `current:` and `alumni:` lists (name, role, dept, photo,
  and a `page:` link). This drives the People index and the home "People" strip.
- Full bios are pages in `_pages/people-<Name>.md` using `layout: person`. Copy an
  existing one as a template. Put photos in `assets/images/`.

### Update the news feed  → `_pages/home.md`

The body of `_pages/home.md` (below the front matter) is the "Latest from the lab"
list — plain Markdown, grouped by `### YEAR`. Add new items at the top.

### Edit navigation → `_data/navigation.yml`. Research themes → `_data/research.yml`.

---

## Automated publication sync (ORCID → pull request)

`.github/workflows/sync-publications.yml` runs weekly (and on demand). It:

1. reads new DOIs from your ORCID record,
2. skips any already in `_data/publications.yml`,
3. pulls author list / venue / year from Crossref, and
4. opens a **pull request** with draft entries — `tags: []` and `senior: false`
   left as TODO for you to fill in.

Nothing changes on the live site until you review and merge that PR. This keeps
the automation reliable (ORCID/Crossref have real APIs — Google Scholar does not)
while leaving the editorial calls (tags, senior authorship) to you.

**One-time setup:** add your ORCID iD as a repo variable —
Settings → Secrets and variables → Actions → **Variables** → New variable,
named `ORCID_ID`, value like `0000-0002-1825-0097`.

**Run it manually:** Actions tab → "Sync publications from ORCID" → Run workflow.

**Run it locally (to preview):**

```bash
ORCID_ID=0000-0002-XXXX-XXXX python scripts/sync_publications.py
git diff _data/publications.yml
```

---

## Where things live

| Path | What |
|------|------|
| `_layouts/` | Page shells: `default`, `home`, `page`, `person`, `post` |
| `_includes/` | `head`, `nav`, `footer`, `authors` (name bolding), `icon` (inline SVG link icons) |
| `_data/` | `publications`, `people`, `research`, `navigation`, `lab_names` |
| `_pages/` | Content pages (home, research, people bios, teaching, guides, handbook, contact) |
| `assets/css/main.scss` | The whole design system (palette, type, components) |
| `assets/js/main.js` | Nav toggle, scroll reveal, publication filters |
| `scripts/sync_publications.py` | ORCID → publications.yml sync |
