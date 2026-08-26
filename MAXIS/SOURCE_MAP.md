# MAXIS SOURCE MAP

| Artifact | Role | Current disposition | Key dependency |
|---|---|---|---|
| `E00 796` | Full E00 assessment candidate | Candidate / inspect against live | Produces assessment result |
| `E00 1800` | Full E00 assessment candidate | Candidate / inspect against live | Produces assessment result |
| `E00.01` | Result bridge | Keep concept, simplify authority | `MAXESS_RESULT_V1` |
| `E00.02` | Isolation/release CSS + gate | Keep as visual gate | `MAXESS_ISOLATION_RELEASE` |
| `E00.03` | Results controller | Strong candidate for sole release authority | `MAXESS_RESULT_V1` |
| `E01` | Score reveal + personal report | Consumer | Result hydration |
| `E02` | Five dimensions | Consumer | `window.MAXESS_RESULT` |
| `E03` | Personal report | Consumer | `window.MAXESS_RESULT` |
| `E04` | Direction spectrum | Consumer | Result + Direction dimension |
| `E05` | AI friction/familiarity | Presentation | Mostly static content |
| `E06` | Naya Supercharger | Presentation | Mostly static/content |
| `E07` | Cinematic conversion/video | Presentation | CTA/video |
| `E08` | Human Maximus ecosystem | Presentation | Offer/navigation |
| `E09` | Membership preview | Presentation | Membership links |

## Canonical runtime graph

```text
                 ┌──────────────────┐
                 │       E00        │
                 │ assessment/score │
                 └────────┬─────────┘
                          │
                          ▼
                MAXESS_RESULT_V1
                          │
                          ▼
                 ┌──────────────────┐
                 │      E00.01      │
                 │ bridge/adapter   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │      E00.03      │
                 │ release authority│
                 └────────┬─────────┘
                          │
                 MAXESS_ISOLATION_RELEASE
                          │
                          ▼
                 ┌──────────────────┐
                 │      E00.02      │
                 │ visual release   │
                 │      gate        │
                 └────────┬─────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │       E01 → E09          │
             │ downstream consumers     │
             └──────────────────────────┘
```

## Current architectural conflict

The existing source does not perfectly match this target graph yet. E00.01 currently contains release behavior, while E00.03 also contains release behavior. E00.03 also validates a stricter contract than E00.01. This should be resolved before more UI work.

## External dependency note

Several sections load images from the separate `SoulSchoolAcademy/MaxRESULTS` repository. That is acceptable for presentation assets, but the assessment/result engine itself should not depend on external HTML execution to calculate or transport the score.
