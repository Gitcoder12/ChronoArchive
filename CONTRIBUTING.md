# Contributing to ChronoArchive

## Adding Historical Data
1. Add entries to `data/timelines.json` (create if missing)
2. Format: `{ id, title, date, category, region, description, sources[] }`
3. Categories: art, science, politics, culture, war, discovery

## Adding a New Timeline View
1. Create a new tab section in `index.html`
2. Filter from the shared data array by category or region
