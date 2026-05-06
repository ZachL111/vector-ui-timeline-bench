# vector-ui-timeline-bench

`vector-ui-timeline-bench` is a compact Lua repository for frontend apps, centered on this goal: Develop a Lua command-oriented project for timeline scenarios with capacity fixtures, allocation and spill reports, and explicit failure cases.

## Project Rationale

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Vector UI Timeline Bench Review Notes

Start with `state pressure` and `view drift`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## Feature Set

- `fixtures/domain_review.csv` adds cases for view drift and state pressure.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/vector-ui-timeline-walkthrough.md` walks through the case spread.
- The Lua code includes a review path for `state pressure` and `view drift`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Architecture

The implementation keeps the scoring rule plain: reward signal and confidence, preserve slack, penalize drag, then classify the result into a review lane.

The added Lua path is deliberately direct, with fixtures doing most of the explaining.

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Test Command

The same command runs the local verification path. The highest-scoring domain case is `stress` at 241, which lands in `ship`. The most cautious case is `stale` at 142, which lands in `ship`.

## Next Improvements

This remains a local project with deterministic fixtures. It does not depend on credentials, hosted services, or live data. Future work should add richer malformed inputs before widening the public API.
