# Datebell

Public pages for the Datebell iPhone app (Thai and English).

- Privacy Policy: https://datebell.github.io/privacy.html
- Support: https://datebell.github.io/support.html

Home: `index.html` (minimal, one screen). Features: `features.html` (new features with real screens, then the full list). Shared `css/site.css` and `js/site.js`. Screens in `img/hero/` and `img/new/`. Both pages keep `?ct=` (App Store campaign link) and `?lang=th|en`.

Service plan prices for the app: `prices/v1/<country>.json` (TH, US, GB, CA, AU, SG). The app checks its country's file at most once a day and uses it only when every verified price in it passes its checks and it is at least as new as the list built into the app. Each plan keeps its official `sourceUrl` and `verifiedOn` date; the app stops offering a price 90 days after `verifiedOn`, so re-check and bump the dates to keep them showing.

Price-rise alert (app 1.8.1+): when a plan's price goes up, keep the new price in `amountMinor` and add `"was": {"amountMinor": <old price>, "changedOn": "YYYY-MM-DD"}` (the day the new price started, never after `verifiedOn`). A subscription saved at exactly the old price, in the same currency and billing cycle, then shows the alert. Leave `was` in place for about 6 months, then remove it. Before merging, check the files with `node scripts/check-price-files.mjs <this repo>/prices/v1` from `mobile/` in the app repository. A weekly price check opens a pull request here; nothing changes for users until it is merged.

This repo is now ahead of `site/` in the app repository for the landing page; the old nn3tt.github.io/Datebell-site stays as it is.
