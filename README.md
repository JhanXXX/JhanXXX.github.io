# Jinghan Xu — academic website

Five Markdown pages, reusable Liquid layouts, and a single stylesheet. GitHub Pages builds the site with Jekyll. No JavaScript, theme, analytics, or remote fonts are required.

## Content and files

| File | Purpose |
| --- | --- |
| `about.md` | Homepage, research interests, contact links |
| `education.md` | Education, awards, skills |
| `publications.md` | Seven bibliography entries grouped by type |
| `experience.md` | Nine research and professional entries, with original project descriptions preserved |
| `steam.md` | Years and full screenshots, newest first |
| `_config.yml` | Site URL and contact profiles |
| `_data/navigation.yml` | Shared navigation |
| `_layouts/default.html`, `_includes/` | Shared page structure |
| `assets/css/style.css` | Responsive styling |
| `assets/steam/` | Original PNG data with proper file extensions |
| `backups/original/` | Original biography and configuration, excluded from publishing |
| `steam remarks/` | Original extensionless screenshots, untouched and excluded from publishing |

## Local preview

With Ruby and Bundler installed:

```sh
bundle install
bundle exec jekyll serve
```

Visit http://localhost:4000. Jekyll rebuilds when content changes; restart it after editing `_config.yml`.

This machine also supports a Python preview:

```sh
python -m pip install -r requirements-preview.txt
python scripts/preview.py
```

Visit http://127.0.0.1:4000. Restart the script after edits. This uses the same Liquid templates and Markdown content, but Python Markdown rather than Jekyll's Kramdown; GitHub's deployment build is the authoritative Jekyll check. Stop with Ctrl+C. Use `--port 4001` if port 4000 is already occupied.

```sh
python scripts/preview.py --build-only
python scripts/check.py --external
```

## GitHub Pages deployment

The intended repository is `JhanXXX/JhanXXX.github.io`, with `url: https://jhanxxx.github.io` and an empty `baseurl`.

1. Commit these source files to that repository's `master` branch.
2. In repository Settings → Pages, select **Deploy from a branch**, **master**, **/(root)**.
3. Wait for the Pages build/deployment to finish. Visit https://jhanxxx.github.io/.

For a project repository, set `baseurl` to `/repository-name`. All internal navigation and assets use `relative_url` to support this.

[GitHub's local Jekyll instructions](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

## Future updates

- The supplied portrait is `assets/profile.jpeg`. Replace this file to update it, or add `assets/profile.png`, which takes priority. The homepage preserves its aspect ratio and omits the image if neither file exists.
- Add bibliography items to the appropriate section of `publications.md`; retain explicit acceptance/submission status and DOI links.
- Add experience entries near the top of `experience.md`; ordering is by current role and most recent end date.
- Add a screenshot as `assets/steam/YYYY.png` and prepend a year heading and image to `steam.md`, following the existing pattern. Images are never cropped.
- Update shared navigation in `_data/navigation.yml`, contact links in `_config.yml`, and visual styling in `assets/css/style.css`.

## Information to confirm

- Portrait supplied and displayed in the redesigned homepage header.
- The source introduction said the PhD had begun, but the education date is November 2026. As of October 10, 2026, the site labels it upcoming.
- MSc completion is dated October 2026 without an exact award date. The site conservatively says expected October 2026; update after confirmation.
- Presentation [3] retains the supplied year 2025 alongside the TRB Annual Meeting 2026 venue. Confirm whether the bibliographic year should be 2026.
- Presentation [6] is listed as oral in the bibliography and in preparation in the experience source. Both distinctions are retained, with in preparation applied to the related publication.
- No extra journal acceptance/publishing status has been inferred. External sites may block automated link checks; see `CHECKS.md`.

The original sources include referees; these were preserved in the backup but not published because no referees section was requested.
