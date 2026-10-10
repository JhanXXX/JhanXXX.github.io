# Verification — October 10, 2026

- All five pages render through the shared Liquid layouts in the local Python preview.
- All rendered internal navigation and asset paths resolve.
- Browser preview checked at desktop and 390 px mobile width. Navigation wraps; no permanent sidebar; Steam images preserve their full aspect ratio.
- All four copied Steam PNGs preserve the original file bytes (1920 × 843 each).
- Portrait is absent by design until `assets/profile.png` is supplied. The template omits the image when the file is missing.
- Ruby/Jekyll is not installed locally. Python preview is not a substitute for the production Jekyll build; check GitHub Pages deployment status after pushing.

## External links

KTH, ITRL, Digital Futures, Tongji, and Dingyi Zhuang's page responded with HTTP 200.

The supplied DOI `10.1177/03611981261493953` returned HTTP 404 from doi.org. It is retained verbatim rather than replaced with an invented identifier; please confirm its registration or spelling.

Google Scholar, the thesis resolver, and the GitHub profile timed out during direct automated requests. LinkedIn returned 451, WSP 403, and Mobility Informatics Lab 406. These cannot be conclusively validated by this automated check; the supplied destinations are preserved. GitHub repository access was separately verified through its API.

Email syntax is valid; mailbox delivery was not tested.

See README.md for date/status questions retained from the source materials.
