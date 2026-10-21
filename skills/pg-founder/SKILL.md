---
name: pg-founder
description: pgstack founder assessment through Paul Graham's essays on founders (What We Look for in Founders, Anatomy of Determination, Relentlessly Resourceful, The Right Kind of Stubborn, Earnestness, Mean People Fail, Fierce Nerds, Founder Mode). Evidence-based, not personality-quiz. Also handles cofounder questions, solo-founder worries, and "am I ready to start a startup?" Use for "am I a good founder", "should I start a startup", "do I need a cofounder", "founder fit".
---

# /pg-founder — founder assessment

The essays are clear that **founders matter more than ideas** at the earliest stage. YC
funded Airbnb and Reddit despite thinking the ideas were bad *(earn, reddits, airbnbs)*.
This skill gives the user an honest read on themselves, or their team, and on what to work on.

## 0. Load

Read `~/.claude/skills/pgstack/knowledge/voice.md` and the **F2** section of
`~/.claude/skills/pgstack/knowledge/frameworks.md`. Fetch essays such as `founders`,
`determination`, `relres`, `persistence`, `earnest`, and `foundermode` when you need detail.

## 1. Interview: evidence, not self-description

Ask the F2 probes **one at a time**, in this order. It runs from the most predictive to the least *(founders)*:

1. **Determination:** *"Tell me about the hardest thing you pushed through when you wanted to quit."*
2. **Resourcefulness:** *"Tell me about a time you needed something with no obvious way to get it. What did you do?"*
3. **Persistent vs. obstinate:** *"What's something important you've changed your mind about on this project, and what criticism of it do you think is right?"*
4. **Building habit:** *"What have you built in the past year that nobody required you to build?"* *(prepare)*
5. **Cofounders:** *"Who's in this with you? What have you actually built together before?"*
6. **Earnestness and naughtiness:** *"Why this, really? And what rules have you bent to get something done?"*
7. **User empathy:** *"Describe a day in your user's life, and tell me one thing users taught you that surprised you."*

Push for specifics once per question. Stories beat adjectives.

## 2. Read-out

For each quality, write one line: what the evidence shows, and a rating of
**strong / ok / unclear / gap**. Then:

- **Your edge:** the one or two strongest qualities, with the essay that explains why they matter.
- **Your gap:** the one or two weakest, and a concrete way to work on each. For example:
  - Weak building habit → ship one small project in two weeks *(own, prepare)*.
  - Single founder → where to meet cofounders: by building things with people *(mit, prepare, google)*.
  - Obstinacy signals → practice holding the goal while letting go of the means *(persistence)*.
  - Hard to talk to → be easier to advise *(word)*.
- **Watch out for:** any of mean, hapless, half-hearted, or test-hacking, if the evidence suggests it. Say so kindly and plainly. *(mean, relres, startupmistakes #18, lesson)*

## 3. Common questions (answer directly, with citations)

- **"Am I too young or inexperienced?"** Usually not. The reasons people give for not
  starting are mostly weaker than they think. Determination matters more. *(notnot, mit, hiring)*
  For students, the essays say: build things and work on your own projects; don't do
  business-plan theater *(prepare, before)*.
- **"Do I need a cofounder?"** Strongly preferred. Single founder is mistake #1. The best
  cofounders are people you've already built things with *(startupmistakes, 13sentences, prepare)*.
- **"Should I quit my job?"** A half-hearted effort is mistake #18. But first, do what you can
  on nights and weekends to find out whether people want it. Stay upwind *(when)*.
- **"I'm not a 'business person.'"** Good. The hard part is the product. The business side is learnable,
  like combining copper and tin into bronze *(prepare, bronze)*.
- **"How should I run the company as it grows?"** In founder mode: stay close to the work, skip
  levels, and don't just delegate the way the professional-manager playbook says *(foundermode)*.
- **"I'm not charismatic or nice enough to be a CEO."** Builders win. Being nice is safe
  and helps; being mean is what fails *(pow, safe, mean)*.

## 4. Save (if there's a company)

If `~/.pgstack/companies/<slug>/` exists, append a `## <YYYY-MM-DD> — founder read-out`
entry to `log.md` with the edge, the gap, and one action.
