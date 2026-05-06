# Vector UI Timeline Bench Walkthrough

I use this file as a small checklist before changing the Lua implementation.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | view drift | 196 | ship |
| stress | state pressure | 241 | ship |
| edge | layout risk | 168 | ship |
| recovery | interaction cost | 176 | ship |
| stale | view drift | 142 | ship |

Start with `stress` and `stale`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

The next useful expansion would be a malformed fixture around state pressure and interaction cost.
