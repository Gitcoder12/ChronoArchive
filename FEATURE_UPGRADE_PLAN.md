# ChronoArchive — Feature Upgrade Plan

**Snapshot:** 2026-11-13

## Objective

A digital heritage prototype that lets visitors explore example countries, historical artefacts and timelines.

## P0 — correctness, scope and safety

- [ ] Define provenance, source citation, date precision, geographic naming and attribution fields for every artefact.
- [ ] Replace placeholder gap analysis with explicit no-result behavior or a documented research method.

## P1 — complete user workflow

- [ ] Add schema validation and deterministic API tests for countries, artifacts and timelines.
- [ ] Implement search/filter by period, region and source with accessible detail views.

## P2 — evaluation and scale

- [ ] Add curated public datasets with licensing checks and a contributor review workflow.
- [ ] Benchmark search quality and detect conflicting dates without silently choosing one.

## Contributor work packages

1. Input contracts and validation with fixture-based tests.
2. Deterministic core workflow and auditable outputs.
3. User-facing explanations, accessibility and error handling.
4. Reproducible evaluation with a baseline and documented limitations.

## Definition of done

- [ ] Setup works from a clean environment.
- [ ] Tests cover normal, missing, malformed and boundary inputs.
- [ ] Demo/sample data and real external data are clearly distinguished.
- [ ] README, tests and activity log agree on actual behavior.
