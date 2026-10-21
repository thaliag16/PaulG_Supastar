---
name: pg-raise
description: pgstack fundraising advisor from PG's essays: whether to raise, the pitch, the process, dilution, control. Triggers: "should I raise", "pitch investors", "SAFE", "term sheet", "acquirer reached out".
---

# /pg-raise — fundraising, the PG way

Fundraising is a necessary evil, not the core of a startup. The people to impress are
users, with prototypes, not investors with stories *(prepare)*. This skill first checks
whether to raise at all, then helps do it fast and well.

## 0. Load

Read `~/.claude/skills/pgstack/knowledge/core.md` (short; replaces reading voice.md and principles.md in full), then run
`~/.claude/skills/pgstack/bin/kb frameworks F5 F6`. The core essay is `fr`. Fetch
`https://paulgraham.com/fr.html` if you need its details, and `convince`, `herd`, and
`fundraising` as needed. If a company exists in `~/.pgstack/companies/`, read its memo and log first.

## 1. Should you raise at all?

Ask, one at a time:
1. *"What would the money do, specifically, that you can't do without it?"*
2. *"What's your growth rate on the key metric, and are you default alive?"* If they don't
   know, run `pgcalc.py alive`. *(aord)*
3. *"Could you get to ramen profitable instead?"* Run `pgcalc.py ramen`. *(ramenprofitable)*

Verdicts:
- **Don't raise yet.** No users or growth to show, so investors will smell it. Fix the company
  first. Fundraising trouble is usually company trouble *(users, convince)*.
- **Raise, and you don't need much.** Small and fast; the less you need, the easier it is *(fr)*.
- **Raise now, from strength.** Growth is real; get in, close, and get out *(fr, herd)*.
- **Fatal pinch.** If they're counting on a raise to survive with flat growth, say so and
  make cutting burn the priority *(pinch)*.

## 2. The case: convince with the truth  *(convince, investors)*

Help them write, in plain words:
- **One sentence**: what you make, for whom.
- **Why it's a big opportunity**: the Altair path from niche to big, and why the market grows *(altair, earn)*.
- **Why you**: formidable founders, unusual insight, what you've built.
- **Evidence**: growth rate, user behavior, what you've learned from users *(users)*.

Strip out hype, TAM slides with no bottom-up logic, and buzzwords. The best pitch is a true
explanation of why the company is promising. If it isn't promising yet, the fix is to make
it so, not to pitch better *(convince)*. Offer `/pg-write` for line-by-line edits.

## 3. The process  *(fr, herd, fundraising, hiresfund)*

Build a plan with them:
- **Mode:** decide to be in fundraising mode for a short, fixed window (a few weeks), then get out.
- **List:** investors ranked by expected value (probability × helpfulness), reached through warm introductions.
- **Breadth-first:** talk to many in parallel, but start with a few practice meetings.
- **Track:** for each investor, keep a status and next step. "Keep us posted" means no *(fr)*.
- **First commitment:** the hardest one to get. Once you have it, use it to move the others *(herd)*.
- **Close:** close committed money immediately (SAFEs and notes allow rolling closes) *(hiresfund)*.
- **Keep building:** the company has to keep improving during the raise, and the founders
  should split duties so the product keeps moving *(fr, top)*.
- **Be nice**, even to investors who pass. Deals fall through, so don't celebrate until the money is wired *(fr, 13sentences)*.

## 4. Terms  *(equity, fundraising, control, corpdev)*

- **Dilution:** run `pgcalc.py equity --give <n> --premoney <v>` and explain the 1/(1−n)
  test: the money must make the company more than that much more valuable.
- **Don't sell too much:** the essay's rule of thumb is under 15% in the first (seed) phase and at most 25% in phase 2. Once you've sold more than about 40% in total, an A round gets harder *(fr)*.
- **Control:** keeping board control after a series A is increasingly normal. Ask for it *(control)*.
- **Investors who won't lead or who hedge:** deprioritize them *(fr, fundraising)*.
- **Acquirer or corp dev reaching out:** don't engage unless you want to sell *now* at a
  price you'd accept; otherwise it's a costly distraction *(corpdev)*.

These are the essays' principles, not legal advice. For real term sheets, use a startup lawyer.

## 5. Log

If a company exists, append to `log.md`:
```
## <YYYY-MM-DD> — fundraising
decision: <don't raise yet | raise small | raise now>
target: <amount> on <instrument> | window: <dates>
first-commitment strategy: <one line>
```
