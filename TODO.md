# TODO

Working task list for **proper-distance-running-training-guidance**. Read this at the start of a work session and keep it current as work completes - check items off with a date, add follow-ups as they surface. Stale TODOs are worse than none. Security debt (if any) is tracked separately in `SECURITY-DEBT.md`.

---

## Open

### 🔴 Needs Patrick

- [x] ~~Sign off on the Boston 2013 note in `ABOUT.md`~~ ✅ done 2026-07-14 (Patrick wrote it: he and his brother finished before the bombs; learned of it on an airport TV; #BostonStrong)
- [ ] **Fill in the three unnamed marathons.** `plw-portfolio`'s `manualData.ts` lists five marathons but only names Boston 2013. Names, dates, and times would let `ABOUT.md` show the full progression.
- [ ] **Consider back-porting the corrected data to `plw-portfolio`.** The 15K/20K entries in `manualData.ts` sit in a `PERSONAL_RECORDS` array but are not all-out efforts. The portfolio presents them as PRs with no caveat; `ABOUT.md` now footnotes them.

### 🟠 Content

- [ ] Add a **masters/aging** page (training past 40: recovery, strength, realistic expectations).
- [ ] Add a **heat, humidity, and altitude** page (pace adjustment, acclimatization).
- [ ] Add a **running form and cadence** page - and be honest that the evidence for form coaching is thinner than the internet suggests.
- [ ] Consider a **women's-specific** section (menstrual cycle and training, RED-S, bone health). Needs real sourcing or it should not ship.
- [ ] `systems/` covers Daniels and McMillan. Consider adding **Pfitzinger** (the standard for serious marathoners) and **Hansons**.

### 🟡 Polish

- [ ] Single-source-of-truth problem: the author's VDOT figures now appear in `ABOUT.md`, `fundamentals/aerobic-system.md`, `concepts/easy-hard.md`, `systems/jack-daniels.md`, and `reference/vdot-and-pace-tables.md`. If one changes they all must. Consider a script that regenerates them.
- [ ] Cross-check that every `**Next:**` link resolves now that the file set has grown.
- [ ] Decide whether the "Companion YouTube Series" is real. It was promised in the old README with no links for the life of the repo; the promise has been removed rather than left dangling. Re-add only if the videos exist.

---

## Done

- [x] ~~Cite the author's credentials: `ABOUT.md` with Boston splits, PR ladder, and the VDOT-gap thesis; byline in `README.md`; worked examples woven into the aerobic-system, easy/hard, and Jack Daniels pages~~ ✅ done 2026-07-14
- [x] ~~Add missing core topics: strength training, injury prevention, fueling and nutrition, race-day execution~~ ✅ done 2026-07-14
- [x] ~~Add inline VDOT and pace tables so the guide is self-contained (computed from Daniels-Gilbert, verified against published anchors, not copied from the book)~~ ✅ done 2026-07-14
- [x] ~~Add beginner and advanced variants of all four training plans~~ ✅ done 2026-07-14
- [x] ~~Add glossary, FAQ, and a training-log template; rewrite README as a real index~~ ✅ done 2026-07-14
- [x] ~~**Fix the plan-mileage bug.** All four original plans stated weekly totals that did not match the workouts under them, always understating (18-wk marathon Week 16 was labelled "55 miles - PEAK" and prescribed 68). Corrected 54 week headings, regenerated every Weekly Mileage Progression table and `**Weekly Mileage:**` header, and added an "If This Is More Volume Than You Want" scaling section to each of the four. All 12 plans now pass an automated day-sum check.~~ ✅ done 2026-07-14
- [x] ~~Footnote the 15K and 20K on the PR ladder as non-all-out efforts (Patrick does not race those distances often), so the VDOT dip is not read as a fitness gap~~ ✅ done 2026-07-14
