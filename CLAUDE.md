# Proper Training for Distance Running

## Overview
A comprehensive markdown guide to distance-running fundamentals - the principles behind
effective training (aerobic base, recovery, periodization, lactate threshold, HR zones),
established training systems (Jack Daniels, McMillan), and ready-to-use training plan
templates for 5K through marathon. Documentation/content repo, not an application.

## Environment
- **Status**: Documentation / content. **This repo is the SOURCE OF TRUTH; it is
  published elsewhere.** Edit the markdown here, then re-vendor into the site.
- **Live URL**: https://achilles.fit/guides - published as the /guides section of
  **achilles** (`~/coding/achilles`), which vendors these files with
  `frontend/scripts/sync-guides.mjs` (`cd frontend && npm run sync:guides`).
  ⚠️ **Editing `achilles/frontend/src/content/guides/` directly is wasted work** -
  the next sync overwrites it. Change it here.
  ⚠️ **A new file only reaches the site after a re-vendor**, and a new *directory*
  also needs a `SECTIONS` entry in that script or its pages are silently skipped.
- **Cloud**: N/A (the published copy is served from achilles' CloudFront)

## Publishing notes
- **Site-hostile markdown to avoid.** The vendoring step rewrites inter-document
  links and backticked path references (`` `../fundamentals/recovery.md` ``) into real
  site links, using the target page's `# ` heading as the label. Two things follow:
  every content file **must** open with a level-1 heading, and a path reference to a
  file that is not published (README, repo furniture) will fail the site's build
  rather than ship dead text.
- **The first paragraph becomes the meta description**, so it needs to stand alone as
  a ~155-character summary. The sync script concatenates opening paragraphs until it
  has 80+ characters and fails the build if it cannot.
- achilles.fit is the canonical home for search purposes; this repo intentionally
  points at it (README banner + repo homepage URL) rather than competing with it.

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
