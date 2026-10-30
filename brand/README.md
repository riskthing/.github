# RiskThing on GitHub: brand assets and settings

Source files and settings for the [riskthing](https://github.com/riskthing) organization's public GitHub presence.

## Files

| File | Use |
|---|---|
| `matrix-r-logo.svg` | The matrix-R logo. Copied from the app (`static/icons/brand/matrix-r-logo.svg` in the private riskthing repo), which stays the source. |
| `riskthing-avatar.png` | Organization profile picture, 500×500. |
| `riskthing-card.png` | Social preview for `riskthing-skill`, 1280×640. |
| `avatar.html`, `card.html` | The layouts the PNGs are rendered from. The logo SVG is inlined. |
| `shot.py` | Renders both HTML files to PNG with Playwright. |

## Regenerate the images

Edit `card.html` or `avatar.html`, then run from this folder:

```bash
uv run --no-project --with playwright python shot.py
```

On a machine without Playwright's Chromium, run `uv run --no-project --with playwright playwright install chromium` once first.

The card follows GitHub's repository social-card template: 1280×640, with everything important at least 40 px inside the edge so nothing gets cropped. Type is Inter (loaded from Google Fonts, as on the booth sheet). The wordmark is bold text beside the logo, as in the app header.

## Messaging

Copy follows the live riskthing.com landing page and `docs/brand/messaging-guide.md` (private repo): the category line is "Risk intelligence for decisions you can't take back". Change the landing page first, then these.

## Where each setting lives

GitHub has no API for uploading these images, so set them in the web UI.

| Setting | Value | Where |
|---|---|---|
| Profile picture | `riskthing-avatar.png` | [Organization profile](https://github.com/organizations/riskthing/settings/profile) |
| Display name | RiskThing | Organization profile |
| Public email | support@riskthing.com | Organization profile |
| Description | Risk intelligence for decisions you can't take back. A live risk register on a NASA-style 5×5, built by a former NASA Flight Director. | Organization profile |
| Social preview | `riskthing-card.png` | [riskthing-skill settings](https://github.com/riskthing/riskthing-skill/settings) → Social preview |
| Org landing page | `profile/README.md` in this repo | Rendered on https://github.com/riskthing |
