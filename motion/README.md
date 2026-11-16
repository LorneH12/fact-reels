# Motion library (Trending Space / fact reels)

Reusable motion-graphics pieces for 9:16 short videos, built as HTML + GSAP and rendered locally. **Pieces** are built and ready to remix; **ideas** are pitched graphics with their approval status and the look picked (A/B/C stills).

- Visual gallery: https://lorneh12.github.io/fact-reels/motion/
- Machine-readable: https://lorneh12.github.io/fact-reels/motion/catalog.json
- Reels using them: https://lorneh12.github.io/fact-reels/ (catalog: https://lorneh12.github.io/fact-reels/catalog.json)

## Built pieces

### M01 · Countdown card

- **Explains:** How long until a date: a big number, the date, where it's on, the same time in hours, then a follow card.
- **Use when:** Launch countdowns, event countdowns, 'X days until'. Any brand: change accent and bgTop/bgBottom.
- **Don't use when:** The number isn't a time span (use a counter or comparison piece instead).
- **Length:** 15 s · built 2026-11-09 · brand look: wanted-level
- **Variables:** days, hours, unit, kicker, weekday, date, year, pc, cta1, handle, accent, bgTop, bgBottom, endHold
- **Remix:** `om set days=7 hours=168 unit=DAYS pieces/M01-countdown-card && om render pieces/M01-countdown-card --workers 3`
- **Used in:** wanted-level-countdown-01 … 10
- Still: https://lorneh12.github.io/fact-reels/motion/stills/M01/13.00s.jpg
- Still: https://lorneh12.github.io/fact-reels/motion/stills/M01/2.40s.jpg
- Still: https://lorneh12.github.io/fact-reels/motion/stills/M01/5.50s.jpg
- Still: https://lorneh12.github.io/fact-reels/motion/stills/M01/9.00s.jpg

## Ideas

| ID | Name | Status | Look | Reuse |
|---|---|---|---|---|
| I01 | A-vs-B magnitude bars | approved (2026-11-11) | not picked | Any 'more X than Y' fact; GTA map sizes (Vice City vs Los Santos). |
| I02 | Ratio dots | approved (2026-11-11) | not picked | Any 'N in M' or percentage fact; poll results; 'only 1 in 10 players…'. |
| I03 | Fact-or-fake stamp | approved (2026-11-11) | not picked | Fact-reels end card; Wanted Level rumour checks (REAL / NOT CONFIRMED / FAKE) with 2–3 short caveats. |
| I04 | Face-off thermometer | approved (2026-11-11) | not picked | Any two readings on one scale: speed, depth, price, time. |
| I05 | Light-delay timeline | approved (2026-11-11) | not picked | Travel times, delays, 'how long ago' facts; GTA in-game vs real time. |
| I06 | Three-part plan panel | approved (2026-11-11) | not picked | Every Wanted Level explainer; fact-reel chapter episodes; '5 tips' posts as 5 tabs. |
| I07 | Early-or-late dial | approved (2026-11-11) | not picked | Worth it / not worth it, hype vs reality, beginner vs pro verdicts. |
| I08 | Race clock + step counter overlay | picked (2026-11-13) | B | Any how-to or speed-run reel: setup walkthroughs, 'X in 60 seconds' facts, app demos (family-chores 'start a chore in 10 seconds'). |
| I09 | Guide line + label on footage | picked (2026-11-13) | B | Science facts on real footage, GTA map routes, app UI callouts. |
| I10 | Highlighted body part / object part | picked (2026-11-13) | B | Anatomy facts, engine parts, planet layers (earth-core reel). |
| I11 | Stacked label ladder | picked (2026-11-13) | B | Countdowns (top 10 skills), step lists, chapter menus. |
| I12 | Score badge + item cut-out (1–10 ranking) | approved (2026-11-15) | not picked | GTA 6 features ranked, body parts by renewal speed, family apps ranked. |

### I01 · A-vs-B magnitude bars

- **From:** trees-vs-stars-reel: "There are more trees on Earth than stars in our galaxy."
- **Why it's new:** Nothing in the library compares two huge numbers. Two bars grow to scale (3 trillion vs 100–400 billion, with the range shown as a faded band), and the winner label lands on the beat.
- **Reuse:** Any 'more X than Y' fact; GTA map sizes (Vice City vs Los Santos).
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I01/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I01/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I01/C.jpg

### I02 · Ratio dots

- **From:** ocean-dive-reel: "So the animals make their own. About three in four of them can glow."
- **Why it's new:** We say '3 in 4' but show nothing that counts. A 4-dot (or 100-dot) grid where the right share lights up one by one makes the ratio visible.
- **Reuse:** Any 'N in M' or percentage fact; poll results; 'only 1 in 10 players…'.
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I02/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I02/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I02/C.jpg

### I03 · Fact-or-fake stamp

- **From:** every fact reel (CTA): "Follow for more facts that sound fake, but aren't."
- **Why it's new:** Our sign-off line is spoken over nothing. A FAKE? stamp flips to a REAL stamp with the source name, which turns the brand promise into a picture and a repeatable end card.
- **Reuse:** Fact-reels end card; Wanted Level rumour checks (REAL / NOT CONFIRMED / FAKE) with 2–3 short caveats.
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I03/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I03/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I03/C.jpg

### I04 · Face-off thermometer

- **From:** earth-core-reel: "Researchers in France measured about six thousand degrees … The Sun's surface is about five and a half thousand."
- **Why it's new:** Two temperatures are said 4 seconds apart and the viewer has to hold the first in their head. One gauge with two needles (core 6,000 °C, Sun 5,500 °C) shows the gap at once.
- **Reuse:** Any two readings on one scale: speed, depth, price, time.
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I04/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I04/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I04/C.jpg

### I05 · Light-delay timeline

- **From:** old-light-reel: "Its light takes about eight minutes and twenty seconds to reach your eyes."
- **Why it's new:** A delay is hard to feel from a number. A line from 'left the Sun' to 'reached you' with a clock running 8:20, then the same line zoomed out to 2.5 million years for Andromeda.
- **Reuse:** Travel times, delays, 'how long ago' facts; GTA in-game vs real time.
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I05/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I05/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I05/C.jpg

### I06 · Three-part plan panel

- **From:** GTA pilot (planned): 'Can you make money clipping GTA 6?': "Three chapters: the claim, how to do it, is it real."
- **Why it's new:** Our chapter reels have a depth HUD but no on-screen chapter list. A panel with three tabs (the third locked until the end) and a progress bar keeps an open loop running for 60–90 s. Our own design in Wanted Level amber/navy.
- **Reuse:** Every Wanted Level explainer; fact-reel chapter episodes; '5 tips' posts as 5 tabs.
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I06/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I06/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I06/C.jpg

### I07 · Early-or-late dial

- **From:** GTA pilot (planned): "Are you early, or already too late?"
- **Why it's new:** A verdict needs a picture. A half-dial needle swings from LATE to EARLY (or any two labels) and settles on the answer.
- **Reuse:** Worth it / not worth it, hype vs reality, beginner vs pro verdicts.
- **Status:** approved
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I07/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I07/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I07/C.jpg

### I08 · Race clock + step counter overlay

- **From:** Instagram reel DfoSh7SM1N5 (GTA clipping tutorial, studied 2026-11-13): "Using GTA 6 to ... in under 40 seconds (Step 1 ... Step 8, with a running stopwatch)"
- **Why it's new:** M01 is a full-screen countdown card. Nothing in the library runs a live stopwatch over footage while numbered steps tick by; the clock is the proof device ('it really is this quick').
- **Reuse:** Any how-to or speed-run reel: setup walkthroughs, 'X in 60 seconds' facts, app demos (family-chores 'start a chore in 10 seconds').
- **Status:** picked, look B picked
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I08/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I08/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I08/C.jpg

### I09 · Guide line + label on footage

- **From:** IG saves review 2026-11-13: fitness saves (posture fix, 28M plays): "Fix your anterior pelvic tilt (dashed line from hip to knee, one label)"
- **Why it's new:** Nothing in the library annotates live footage; a dashed line draws on, a pill label pops at its end, then a second line shows the corrected angle.
- **Reuse:** Science facts on real footage, GTA map routes, app UI callouts.
- **Status:** picked, look B picked
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I09/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I09/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I09/C.jpg

### I10 · Highlighted body part / object part

- **From:** IG saves review 2026-11-13: fitness saves (muscle highlight on a 3D figure): "the muscle that does the work glows red on a grey figure"
- **Why it's new:** Our Blender pieces show whole objects; none highlights one part and labels it while the rest dims.
- **Reuse:** Anatomy facts, engine parts, planet layers (earth-core reel).
- **Status:** picked, look B picked
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I10/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I10/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I10/C.jpg

### I11 · Stacked label ladder

- **From:** IG saves review 2026-11-13: sports drill reel (SPEED / AGILITY / … rows): "eight stacked rows, each a word + a small looping demo"
- **Why it's new:** No list piece where each row is a live mini-scene; good for 'N things' countdowns.
- **Reuse:** Countdowns (top 10 skills), step lists, chapter menus.
- **Status:** picked, look B picked
- Still (A): https://lorneh12.github.io/fact-reels/motion/stills/I11/A.jpg
- Still (B): https://lorneh12.github.io/fact-reels/motion/stills/I11/B.jpg
- Still (C): https://lorneh12.github.io/fact-reels/motion/stills/I11/C.jpg

### I12 · Score badge + item cut-out (1–10 ranking)

- **From:** IG save 2026-11-15: 'Expert ranks supplements for focus 1–10': "Ginkgo… two out of ten"
- **Why it's new:** No piece ranks items with a big score badge over a cut-out of the thing being ranked; ascending order saves the best for last.
- **Reuse:** GTA 6 features ranked, body parts by renewal speed, family apps ranked.
- **Status:** approved
- Stills: not rendered yet
