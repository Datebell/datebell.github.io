# Datebell

Public pages for the Datebell iPhone app (Thai and English).

- Privacy Policy: https://datebell.github.io/privacy.html
- Support: https://datebell.github.io/support.html

Landing page: `index.html` (screenshots in `img/v17/`, from the 1.7.0 App Store set). Holiday data for the app: `holidays/v1/`.

Service plan prices for the app: `prices/v1/<country>.json` (US, GB, CA, AU, SG). The app checks its country's file at most once a day and uses it only when every verified price in it passes its checks and it is at least as new as the list built into the app. Each plan keeps its official `sourceUrl` and `verifiedOn` date; the app stops offering a price 90 days after `verifiedOn`, so re-check and bump the dates to keep them showing. A Thai file (`TH.json`) can be added the same way when the Thai prices are re-checked.

This repo is now ahead of `site/` in the app repository for the landing page; the old nn3tt.github.io/Datebell-site stays as it is.
