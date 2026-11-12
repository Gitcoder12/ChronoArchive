# ChronoArchive

**A prototype for exploring cultural heritage records through countries, artifacts, and timelines.**

[![License](https://img.shields.io/badge/license-see%20LICENSE-lightgrey)](LICENSE)

ChronoArchive is an early-stage digital-heritage concept. The repository contains a static HTML exploration page and a small Express API skeleton for country, timeline, artifact, museum, and historical-gap endpoints.

## Features in the Current Prototype

- Static country cards and example detail dialogs.
- Express endpoints for countries, timelines, artifacts, and museums.
- A placeholder gap-detection endpoint.
- Clear separation between the browser page and API server.

## Tech Stack

HTML · CSS · JavaScript · Node.js · Express · CORS

## Quick Start

Install the server dependencies:

```bash
git clone https://github.com/Gitcoder12/ChronoArchive.git
cd ChronoArchive
npm install
node server.js
```

The API listens on `http://localhost:5000` by default.

For the static page, serve the repository root with a local HTTP server in a second terminal:

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

The API arrays are currently empty and are not connected to an archive or museum data source. The gap-detection function is a stub. The static page contains example content; it is not a complete or verified cultural-heritage catalogue. The npm package's original start script pointed to a missing `index.js`; use `node server.js` for the committed API server.

## License

See [LICENSE](LICENSE).
