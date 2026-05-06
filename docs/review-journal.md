# Review Journal

The repository goal stays the same: develop a Lua command-oriented project for timeline scenarios with capacity fixtures, allocation and spill reports, and explicit failure cases. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its frontend apps focus without claiming live deployment or external usage.

## Cases

- `baseline`: `view drift`, score 196, lane `ship`
- `stress`: `state pressure`, score 241, lane `ship`
- `edge`: `layout risk`, score 168, lane `ship`
- `recovery`: `interaction cost`, score 176, lane `ship`
- `stale`: `view drift`, score 142, lane `ship`

## Note

This file is intentionally plain so the fixture remains the source of truth.
