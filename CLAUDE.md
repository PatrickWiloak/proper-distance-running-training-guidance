# Proper Training for Distance Running

## Overview
A comprehensive markdown guide to distance-running fundamentals - the principles behind
effective training (aerobic base, recovery, periodization, lactate threshold, HR zones),
established training systems (Jack Daniels, McMillan), and ready-to-use training plan
templates for 5K through marathon. Documentation/content repo, not an application.

## Environment
- **Status**: Documentation / content (no deployment)
- **Live URL**: N/A
- **Cloud**: N/A

## Tech Stack
- Markdown only; no build system, no source code.

## Common Commands
None - edit markdown directly and commit with git.

## Project Structure
```
ABOUT.md        author credentials (Boston 2013 2:55:13, PR ladder) + the VDOT-gap thesis
fundamentals/   principles, workout types, aerobic system, recovery, progression,
                strength training, injury prevention, fueling and nutrition
concepts/       HR zones, VO2max/economy, lactate threshold, easy/hard rule, race-day execution
systems/        Jack Daniels, McMillan, comparison/how-to-choose
templates/      5K/10K/half/marathon plans at beginner, intermediate, advanced + training log
visuals/        periodization guide, HR-zones table
reference/      VDOT and pace tables, glossary, FAQ
README.md       index + overview
```

## House Style
- **No em dashes or en dashes anywhere.** Use a regular hyphen ` - `. Hard rule.
- Every content page ends with `---`, a numbered `## References` section, then a `**Next:**` link.
- **Never fabricate a citation, DOI, or PMC ID.** Fewer real references beats more fake
  ones. If unsure a paper exists, cite it without the DOI or leave it out. Readers are
  invited in the README to check the sources, so they must survive checking.
- Where evidence is weak or contested (shoe prescription, stretching), say so plainly
  rather than overclaiming.

## Codebase Invariants
- **The VDOT numbers are computed, not copied.** `reference/vdot-and-pace-tables.md` is
  generated from the published Daniels-Gilbert formulas (see the script embedded in that
  file), NOT reproduced from Daniels' copyrighted tables. If you change a VDOT figure
  anywhere in the repo, regenerate it with that script rather than editing by hand, and
  keep it consistent across `ABOUT.md`, `fundamentals/aerobic-system.md`,
  `concepts/easy-hard.md`, and `systems/jack-daniels.md`, which all cite the same
  worked example.
- **The author's real race data is load-bearing content, not decoration.** The Boston
  2013 splits and the PR-to-VDOT ladder are used as worked examples across several
  pages. They are real. Do not round, embellish, or invent additions to them.
- **Training-plan arithmetic must sum.** Every weekly schedule states a mileage total;
  the daily miles must actually add up to it. Verify before committing plan edits.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
