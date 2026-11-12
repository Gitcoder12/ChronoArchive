# ChronoArchive

**A prototype for exploring cultural heritage records through countries, artifacts, and timelines.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

ChronoArchive is an early-stage digital-heritage concept. The repository contains a self-contained static HTML exploration page and a small Express API skeleton for country, timeline, artifact, museum, and historical-gap endpoints.

## Features in the Current Prototype

- Search and filter the two bundled sample country cards.
- Open example detail dialogs for Italy and Egypt.
- Express endpoints for countries, timelines, artifacts, and museums.
- A placeholder gap-detection endpoint.

## Tech Stack

HTML · CSS · Vanilla JavaScript · Node.js · Express · CORS

## Quick Start

Install the server dependencies and start the API:

```bash
git clone https://github.com/Gitcoder12/ChronoArchive.git
cd ChronoArchive
npm install
npm start
```

The API listens on `http://localhost:5000` by default. Check the server syntax with:

```bash
npm run check
```

To open the static browser demo, serve the repository root in a second terminal:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## API Endpoints

| Method | Endpoint | Current behavior |
|---|---|---|
| GET | `/api/countries` | Returns the in-memory country array |
| GET | `/api/timelines` | Returns the in-memory timeline array |
| GET | `/api/artifacts` | Returns the in-memory artifact array |
| GET | `/api/museums` | Returns the in-memory museum array |
| GET | `/api/gaps` | Calls a placeholder that currently returns an empty list |

## Scope and Limitations

The API arrays are currently empty and are not connected to an archive or museum data source. The gap-detection function is a stub. The static page contains two illustrative country entries; it is not a complete or verified cultural-heritage catalogue. Browser content and API responses are not yet connected.

## License

MIT. See [LICENSE](LICENSE).
