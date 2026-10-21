# PaulG_Supastar

**Invest like the best — a Paul Graham agent for Claude Code.** (Internally the skill pack is called *pgstack*.)

A gstack-style set of Claude Code skills that act as a startup advisor built on **all 234
of Paul Graham's essays**. It turns a raw idea into a structured company and keeps you
honest about it week by week, using the principles in the essays and citing them.

> pgstack is an AI advisor modeled on Paul Graham's published writing. It is not Paul
> Graham, and it isn't affiliated with him or Y Combinator. It paraphrases and cites the
> essays and links to the originals at paulgraham.com; read them.

## Skills

| Command | What it does | Built mainly on |
|---|---|---|
| `/pg` | Entry point. Answers any question with citations, or routes to the skill below that fits. | everything |
| **`/pg-office-hours`** | **Flagship.** One question at a time, it takes an idea through origin, the well, traps, v1, ambition, power, and the metric and money, then writes a one-page **Company Memo** and a this-week assignment. | startupideas, ds, growth, powerful, altair, aord |
| `/pg-idea` | Scores an idea on 10 tests, compares several ideas, or helps you notice an idea if you don't have one. | startupideas, organic, schlep, ambitious, bronze |
| `/pg-founder` | An evidence-based read on you as a founder, plus cofounder and solo-founder questions. | founders, determination, relres, persistence, earnest |
| `/pg-growth` | Weekly check-in: logs the metric, computes the growth rate and default-alive status, finds the #1 problem, sets a one-week experiment. | growth, ds, users, aord, ramenprofitable |
| `/pg-raise` | Whether to raise at all, the pitch, the process, dilution, and control. | fr, convince, herd, equity, corpdev |
| `/pg-checkup` | Diagnoses a stuck company against the 18 mistakes and other failure modes. | startupmistakes, die, pinch, users |
| `/pg-write` | Edits a YC application, pitch, memo, or landing page to be plain, true, and strong. | simply, talk, useful, words, users |
| `/pg-path` | What to work on: startup, job, or school, and how to do great work. | greatwork, superlinear, when, own, prepare |

Plus a **`paul-graham` subagent** (`agents/paul-graham.md`) that any Claude Code session can
call for a PG-lens second opinion.

## Install

```bash
git clone https://github.com/thaliag16/PaulG_Supastar.git ~/PaulG_Supastar
cd ~/PaulG_Supastar && ./setup.sh
```

Keep the clone where it is: the installed skills are symlinks into it, so `git pull` updates them.

This symlinks `skills/*` into `~/.claude/skills/`, the repo itself to
`~/.claude/skills/pgstack` (where the skills find `knowledge/` and `bin/`), and the agent
into `~/.claude/agents/`. Use `./setup.sh --copy` to copy instead, and
`./setup.sh --uninstall` to remove it. Restart Claude Code afterwards.

## What's inside

```
knowledge/
  essay-index.md     all 234 essays: title, date, file, one-line takeaway, grouped by theme
  principles.md      104 core principles, each cited to its essays
  frameworks.md      F1 idea tests · F2 founder tests · F3 "make it powerful" · F4 growth ·
                     F5 survival math · F6 fundraising · F7 Company Memo template · F8 weekly loop
  failure-modes.md   the 18 mistakes plus 23 more, each with a diagnostic question and fix
  voice.md           how the advisor talks, and its honesty rules (no invented quotes, always cite)
bin/pgcalc.py        default alive/dead, growth compounding, weekly rate, equity equation, ramen gap
skills/              the nine skills above
agents/              paul-graham subagent
```

State is kept in `~/.pgstack/companies/<slug>/`: `memo.md` (the Company Memo) and
`log.md` (an append-only weekly log of the metric, survival status, #1 problem, and
experiment). This lets `/pg-growth` and `/pg-checkup` see the trend over time.

## The calculator

```bash
python3 bin/pgcalc.py alive  --cash 600000 --burn 80000 --revenue 10000 --growth 0.08
python3 bin/pgcalc.py growth --rate 0.07 --period week --start 1200
python3 bin/pgcalc.py weekly --values 100,106,113,121,128
python3 bin/pgcalc.py equity --give 0.1 --premoney 9000000
python3 bin/pgcalc.py ramen  --revenue 3000 --living 7000 --growth 0.2
```

It reproduces the math in *How to Earn a Billion Dollars*: 93%/month reaches 500× in about
9.45 months, and 15%/month for 60 months is about 4,384×.

## A suggested rhythm

1. `/pg-office-hours` once per idea, which gives you a memo and an assignment
2. `/pg-growth` every week after launch
3. `/pg-checkup` whenever growth stalls for three or more weeks
4. `/pg-raise` only once the numbers make the case
5. `/pg-write` before anything important goes out

## Keeping it current

PG publishes a few essays a year. To add one: read it, add a line to the right section of
`knowledge/essay-index.md`, and add or update any principles it changes in `principles.md`
(newer essays take precedence where they update older views).

Coverage was checked against paulgraham.com/articles.html as of October 2026 (234 entries,
newest: *Making Startups Powerful*, September 2026).
