---
name: pg-growth
description: pgstack weekly growth check-in: logs the key metric, growth rate, default alive/dead, the #1 problem, and a one-week experiment. Triggers: "weekly check-in", "growth is flat", "how do I get users".
---

# /pg-growth — the weekly loop

A startup is a company designed to grow fast *(growth)*. This skill is the weekly office
hour: measure, find the problem that matters most, and test one fix within a week *(users)*.

## 0. Load and find the company

Read `~/.claude/skills/pgstack/knowledge/core.md` (short; replaces reading voice.md and principles.md in full), then run
`~/.claude/skills/pgstack/bin/kb frameworks F4 F5 F8`.

```bash
ls -1 ~/.pgstack/companies/ 2>/dev/null
```

If there's a company, read its `memo.md` and the last ~40 lines of `log.md`, and pull the
metric history from previous `metric:` lines. If there isn't one, ask for the one-sentence
description and the key metric, then create `~/.pgstack/companies/<slug>/log.md`.

## 1. The number

Ask: *"What's the key metric this week, and what was it last week?"* If they don't have one
key metric, help them pick it: revenue if they charge, otherwise the count of users getting
real value (weekly active users who do the core action). Not signups, not pageviews.
*(growth, 13sentences: you make what you measure)*

Run it over the history:

```bash
python3 ~/.claude/skills/pgstack/bin/pgcalc.py weekly --values <oldest,...,newest>
python3 ~/.claude/skills/pgstack/bin/pgcalc.py growth --rate <weekly rate> --period week --start <current>
```

Read it out plainly: "You grew X% this week. At that rate you'd be N× bigger in a year."
Benchmarks: around 1%/wk means not there yet, 5–7% is good, and 10% is exceptional *(growth)*.
If the numbers are tiny, remind them that the rate matters more than absolute size early on
*(growth, earn)*.

## 2. Survival (monthly, or whenever money changes)

If they've given cash, burn, and revenue (or if it's been four weeks or more since the last
check), run:

```bash
python3 ~/.claude/skills/pgstack/bin/pgcalc.py alive --cash <c> --burn <b> --revenue <r> --growth <monthly>
```

If they're **default dead**, this outranks everything else. Name the fatal pinch if it
applies *(pinch)*, and make cutting burn or getting to ramen profitability the week's priority
*(aord, ramenprofitable)*.

## 3. The problem that matters most

Ask: *"What are you most worried about right now? List everything."* Then **you** rank the
list by what kills the company if it's ignored. Founders often get this order wrong
*(users)*. Common re-rankings:
- "We can't raise" → the real problem is growth *(users)*.
- "Users don't come" → the product isn't good enough; would *you* use it? *(users)*
- "We need more features" → you need to talk to users and watch them use it *(ds)*.
- "Competitor X launched" → fear the right things; competitors rarely kill startups *(startuplessons, die)*.

Say the #1 problem in one sentence.

## 4. One experiment, one week

Propose one to three experiments that attack the #1 problem, each runnable within a week,
each with a measurable result. Draw on **do things that don't scale** *(ds)*:
- Recruit users by hand: specific people and channels, done by the founders themselves.
- Onboard users personally and watch them without helping; fix things the same day.
- Do the hard part manually behind the scenes.
- Narrow to the group where usage is strongest, then dominate it.
- Give customer service so good it surprises people.
- Find whatever users are "misusing" the product for, and lean into it *(powerful)*.

Ask what they learned from users this week. If the answer is "nothing," that's the problem *(users)*.

## 5. Guard the founders' minds

Quick check:
- Is fundraising, a dispute, or anything else taking over **the top idea in your mind**? *(top)*
- Are makers getting **uninterrupted blocks** of time? *(makersschedule)*
- Any **fake work** this week, meaning activity users wouldn't notice? *(selfindulgence)*

## 6. Log it

Append to `~/.pgstack/companies/<slug>/log.md`:

```
## <YYYY-MM-DD> — weekly
metric: <name> <prev> → <now> (<+x.x%>/wk) | compound <y.y%>/wk over <n> wks
default: <alive|dead|unchecked>
#1 problem: <one line>
experiment: <what, success criterion, due date>
learned from users: <one line>
```

End with the experiment as this week's assignment, and say they should come back next week
with the number.
