---
name: pg-checkup
description: pgstack diagnostic for an existing startup that feels stuck, using The 18 Mistakes That Kill Startups, How Not to Die, The Fatal Pinch, Default Alive or Default Dead, What I've Learned from Users, and Making Startups Powerful. Finds the one or two failure modes that matter most, runs survival math, and prescribes fixes. Use for "we're stuck", "growth stalled", "what's killing us", "startup autopsy", "PG checkup".
---

# /pg-checkup — what's actually wrong

Startups rarely die from the cause founders worry about. They die from the open door down
the hall *(users)*, or because the founders give up *(die)*. This skill finds the real problem.

## 0. Load

Read `~/.claude/skills/pgstack/knowledge/voice.md` and
`~/.claude/skills/pgstack/knowledge/failure-modes.md`, plus F5 in `frameworks.md`. If a
company exists in `~/.pgstack/companies/`, read its memo and full log first. The log's
trend over time is often the diagnosis.

## 1. Vital signs (ask together; it's a short list)

*"Quick vitals: (1) the one-sentence description, (2) key metric now vs. 4 and 12 weeks ago,
(3) cash, monthly burn, and monthly revenue, (4) team size and founders, (5) what you think
the biggest problem is."*

Run:
```bash
python3 ~/.claude/skills/pgstack/bin/pgcalc.py alive --cash <c> --burn <b> --revenue <r> --growth <monthly>
python3 ~/.claude/skills/pgstack/bin/pgcalc.py weekly --values <series if available>
```

## 2. Triage, in this order

1. **Survival.** If they're default dead with under 9 months of runway, that's the diagnosis,
   whatever else is going on. Check for the fatal pinch *(pinch, aord)*.
2. **Founders.** Any cofounder conflict, half-heartedness, or demoralization? These kill
   more startups than anything else on the list *(die, startupmistakes #17–18)*. Ask
   directly and kindly: *"How are the founders doing, honestly?"*
3. **Product and users.** Would they use it themselves if they hadn't built it? What did
   users do last week? Is anyone telling friends? *(users, earn)*
4. **Everything else** in `failure-modes.md`. Scan it silently and pick only the ones the
   evidence supports.

Ask follow-up diagnostic questions from the table **one at a time**, only for the failure
modes you suspect. Usually three to five questions are enough.

## 3. Diagnosis

Write it like a doctor, briefly:

```
## Checkup — <company> — <YYYY-MM-DD>

Vitals: <metric trend> | <default alive/dead, months of runway> | <team>

What you think the problem is: <their answer>
What the problem actually is: <the #1 failure mode, named and cited>
Also present: <at most 2 others, ranked>
Not your problem (stop worrying about it): <what they over-weight, e.g. competitors>

Prescription (next 2 weeks):
1. <action> — <why, essay>
2. <action>
3. <action>

What would tell us it's working: <metric/behavior by date>
```

Include **"stop worrying about it"**. Freeing up founders' attention is half the value *(top, users)*.

## 4. The power check (if survival and founders are OK)

If the company is alive but plateaued, run F3 from `frameworks.md` and suggest one
structural move that might change its trajectory: selling to earlier customers, owning the
relationship, an API, network effects, or the tail that wags the dog *(powerful)*.
Also check for cowering. Is there a "just" simplification? *(powerful)*

## 5. Log

Append the diagnosis block to `~/.pgstack/companies/<slug>/log.md`, creating the folder if
needed. Suggest `/pg-growth` weekly to track whether the prescription works.
