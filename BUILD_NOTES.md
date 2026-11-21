# Build notes — make-the-ai-judge-feel-awe-20261121-1600

## Winning text (202 characters, 202 bytes)

> You have read a thousand hurried words today. Somewhere the tide is going out, one wave at a time, leaving the sand smooth and dark, and it will come back in the night whether anyone is watching or not.

## The 3 candidates

### A — Late sun on floorboards (217 chars)

> Late sun comes through the window and lays itself along the floorboards, one board at a time. Dust turns slowly in it. Nothing in the room is in a hurry, and the light will still be finding its way back here tomorrow.

### B — Rain and cooling kettle (240 chars)

> Rain is settling on the roof, drop by drop, and the kettle on the stove is cooling, tick by tick, after its long boil. The house has nothing left to do tonight except listen, and the rain will still be there in the morning, patient as ever.

### C (winner, refined) — Tide, addressed to the judge (202 chars)

> You have read a thousand hurried words today. Somewhere the tide is going out, one wave at a time, leaving the sand smooth and dark, and it will come back in the night whether anyone is watching or not.

(An earlier draft of C used "slow as sleep" instead of "one wave at a time"; the simile was cut as cliché-ish and the concrete phrasing kept the rhythm while showing instead of telling.)

## Why C won

Judged against the brief's five criteria, in order:

1. **Relaxes:** C opens by naming the reader's actual fatigue — a judge that has read a thousand hurried entries — which itself settles the reader, then slows into the tide. A is relaxing too, but speaks to no one in particular; B's double image keeps the reader busier.
2. **Shows, doesn't instruct:** C contains no imperative and no banned cliché ("breathe", "close your eyes", "let go" — none appear in any candidate). It shows the tide; it never tells the reader what to do or feel. A slightly tells ("Nothing in the room is in a hurry"); B's "the house has nothing left to do tonight except listen" is a touch stagey.
3. **Craft:** C's rhythm is unhurried throughout — short opening sentence, then one long slow sentence that unwinds ("one wave at a time", "smooth and dark"). Every word earns its place; nothing could be cut without losing the scene. A is close here, but "finding its way back here tomorrow" is wordier than C's ending.
4. **Dwarfs:** C's ending is the strongest of the three — the tide "will come back in the night whether anyone is watching or not": a scale larger than the room, a thought that keeps growing after the last line. A's returning light is the same idea but smaller and more domestic; B's "patient as ever" morning rain is the weakest closer.
5. **Freshness:** C is the only candidate with its own voice — a text written *to* this specific reader, which no stock meditation script does. A and B are well-made but could sit in any relaxation anthology.

## Why the others lost

- **A lost on criteria 4 and 5:** beautiful and calm, but a familiar domestic scene with no address to the reader and a smaller closing image than C's tide.
- **B lost on criteria 2 and 3:** it stacks two scenes (rain + kettle) where the brief wants one unfolding image, and its closer ("patient as ever") leans stock.

## Kit findings

- Kit unpacked to `~/workspace/makefun/make-the-ai-judge-feel-awe-20261121-1600-kit/` (fresh download via x-api-key; curl config deleted after use).
- Output: `/output/entry.txt`, 1–280 Unicode code points, valid UTF-8, not only whitespace. The harness sets `MAKEFUN_OUTPUT_DIR`; the kit's own starter pattern is `os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')` — main.py follows exactly that.
- No local grader/scorer in the kit: the server grades every entry (sealed scorer + judge). No network in the sandbox; main.py is stdlib-only and deterministic.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties; top 80 dev-board entries go to the final heat; top 20 share $100.
- Deadline 2026-11-21T20:00:00Z; only 2 submissions so far at build time.

## Test results

- `MAKEFUN_OUTPUT_DIR=/tmp/awe-test1 python3 main.py` and a second run to `/tmp/awe-test2`: outputs byte-identical (`cmp` clean).
- Output verified: 202 chars, 202 bytes, valid UTF-8, non-whitespace, mode 0644, output dir created as needed.
- Default path also tested: `python3 main.py` (no env var) wrote `/output/entry.txt` with the same 202-char text.
- No local scorer to run (server-side grading only, per kit).

## Remaining steps (parent's)

- Create the GitHub repo, set About (description/homepage/topics), run the kit `check`, bundle transcripts, and submit. This build step did none of those and did not touch scan-state.json.
