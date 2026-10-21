---
name: pg-idea
description: pgstack fast idea stress-test using Paul Graham's idea essays (How to Get Startup Ideas, Schlep Blindness, Organic Startup Ideas, Frighteningly Ambitious, the Altair test, Making Startups Powerful). Scores one idea, compares several, or helps someone with no idea find one by noticing rather than brainstorming. Use for "is this a good startup idea", "rank my ideas", "I don't have an idea", "PG idea check".
---

# /pg-idea — idea stress test

## 0. Load

Read `~/.claude/skills/pgstack/knowledge/voice.md` and the **F1** and **F3** sections of
`~/.claude/skills/pgstack/knowledge/frameworks.md`. For depth, fetch
`https://paulgraham.com/startupideas.html` (the core essay) when you need its details.

## Mode A — One idea

1. If the user gave only a few words, ask **one** clarifying question: who it's for, and
   where the idea came from.
2. Score the ten **F1** tests (0/1/2). For each, write one line of reasoning with an essay
   citation. Where you're guessing for lack of information, mark it `?` instead of scoring
   it. Don't fake confidence.
3. Give the **shape**:
   - **Well-shaped**: a narrow, deep need. Good.
   - **Shallow and wide**: many people want it a little. Warn.
   - **Sitcom**: sounds plausible, nobody urgently wants it. Say so plainly.
   - **Tarpit**: many have tried and failed for structural reasons.
   - **Altair-like**: looks like a toy now and could become huge. Great, if the founders are strong.
4. **The best version of this idea.** Run F3 and the "just" move to propose a sharper,
   narrower-start, bigger-ambition version. This is often the most valuable part of the answer.
5. **The single test that would tell you most, fast.** It should be something they can do
   in a week, and it should involve real users, such as "Get 10 people from <the group> to use a
   manual version by Friday."
6. Offer `/pg-office-hours` to turn it into a full Company Memo.

Format:

```
## <Idea, in one plain sentence>

Shape: <well-shaped | shallow | sitcom | tarpit | Altair-like>   Score: <x>/20  (? = unknown)

| Test | Score | Why |
|---|---|---|
...

The real problem: <the #1 issue>
Better version: <reframe>
This week's test: <one action>
```

## Mode B — Compare several ideas

Score each briefly (same table, but terse), then rank them. The tiebreaker favors the one
the founder is **most genuinely excited about and best placed to build**: the essays say
this matters most for big outcomes *(when, greatwork, organic)*. Say plainly which one you'd
work on and why, and what you'd have to see to change that ranking.

## Mode C — No idea yet

**Don't brainstorm a list of ideas for them.** The essays say this is the wrong method
*(startupideas, earn, prepare)*. Instead, ask the noticing questions from F1 **one at a
time**:

1. What do you wish someone would make for you? *(organic)*
2. What have you built, or what are you building, just for fun? *(when, google, prepare)*
3. What tedious, annoying thing do you and the people around you just put up with? *(schlep)*
4. What do you know well that seems strange, broken, or missing to you, even if others don't notice? *(getideas, startupideas)*
5. What change in technology or the world are you closer to than most people? *(startupideas: live in the future)*

From their answers, point out two or three **candidate problems** (not polished pitches),
say why each might be a well, and give the cheapest way to test each one. If nothing comes
up, the advice is the essays' advice: go build things you find interesting, with people
you'd want as cofounders, and the ideas will come from that *(prepare, when, own)*.
Give a concrete first project.
