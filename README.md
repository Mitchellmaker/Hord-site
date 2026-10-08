# Hord website — local review

Three buildless static pages: `/`, `/support/`, `/privacy/`. Serve this repository root with `python3 -m http.server 8765 --bind 127.0.0.1` and visit http://127.0.0.1:8765/. Root-relative links require a web server; opening HTML files directly is not supported.

No frameworks, runtime JavaScript, analytics, cookies, external fonts, embeds or contact form. Approved supplied artwork is optimised into local assets. NB image copies only have transparent outer margins removed; the phone/UI is preserved. Master assets are untouched.

## Before publication (not authorised in Phase 2)

- Confirm the final domain. Set `public_origin` in `site-config.json`, then run `python3 scripts/configure-origin.py`. This adds canonical URLs, Open Graph URLs, absolute social-image URLs, a populated sitemap and public robots rules. Current review robots disallows indexing; current sitemap is deliberately empty rather than asserting a fictional domain.
- Confirm the real App Store URL. `app_store_url` is currently null; the visible availability panel is plain non-interactive content. Replace both panels in `index.html` with an accessible link after approval, and use an approved Apple badge if desired. The JSON key alone does not activate the CTA.
- Confirm the release facts and review the privacy wording, including support information and hosting practices.
- Test the chosen host's clean directory URLs at the root origin; no SPA fallback is required.

Do not commit, push, deploy or change the Hord app without separate authorisation.
