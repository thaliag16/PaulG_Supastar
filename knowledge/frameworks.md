# Frameworks — the essays turned into tests you can run

Each framework is a set of questions with what a good answer and a bad answer sound like.
Skills run these **one question at a time** and push for specifics. Scores are a tool for
focus, not a verdict. PG funded Airbnb while thinking the idea was bad, because of the founders.

---

## F1. Idea tests  *(startupideas, organic, schlep, ambitious, altair, bronze, swan, brandage, powerful)*

Score each 0 (fails), 1 (unclear or weak), 2 (strong, with evidence).

| # | Test | Ask | Strong answer | Weak answer |
|---|------|-----|---------------|-------------|
| 1 | **Organic** | Do *you* want this? Did the idea come from your own life or work? | "I hit this problem every week at my job; I hacked a script for myself." | "I read that the market is $40B." |
| 2 | **Can build** | Can you (the founders) build v1 yourselves, in weeks? | "I have a prototype." | "We'll hire engineers once we raise." |
| 3 | **The well** | Who wants this *urgently*, right now? Name them. Would they use a crappy v1 from strangers? | A specific, small group with burning need. | "Everyone could use this." (shallow and broad) |
| 4 | **Non-obvious** | Why haven't others done this? What do you see that they don't? | Founder is living in the future, has unusual knowledge, or the idea hides behind a schlep. | "No one has thought of it." (rarely true) |
| 5 | **Sitcom check** | Is this an idea that *sounds* plausible but nobody actually needs? | Real pull: users asking, paying, hacking workarounds. | Only hypothetical users and enthusiasm in surveys. |
| 6 | **Tarpit check** | Have many people tried this and failed? Why? What's different now? | A clear account of why the previous failures happened and what changed. | Unaware of prior attempts. |
| 7 | **Schlep / unsexy advantage** | Is there a tedious or unglamorous part that scares others away? | Yes, and the founders are willing to do it. | The idea is all clever software, no schlep, so it's easy to copy. |
| 8 | **Altair test** | Why might this look lame now but be huge later? What does it grow into? | A specific path from a toy-like start to something big. | No path beyond the initial niche, or no toy-like start at all. |
| 9 | **Money check** (bronze) | How does it make money, roughly? Is this the idea in your space most likely to? | Plausible: users pay, or money flows through it. | "We'll figure out monetization later" plus no sign of users who'd pay. |
| 10 | **Substance, not brand** | Does it win on a real difference or on image? | Real, measurable improvement. | Differentiation is mostly aesthetic or positioning. |

**Reading the scores:** 1–3 are gating; a zero on any of them is the main problem to fix,
whatever the total. 4–10 tell you what to probe. Keep in mind that "looks bad but founders
are strong" is a legitimate profile (Airbnb). Never kill an idea only because it sounds lame.

**Generating ideas when the user has none:** don't brainstorm; run these questions instead.
- What do you wish someone would make for you? *(organic)*
- What's missing that seems obvious to you because you live in the future? *(startupideas)*
- What annoying, tedious problem do you and your colleagues tolerate? *(schlep)*
- What are you working on for fun? Could it be the real thing? *(when, prepare, google)*
- What seems strange, broken, or missing at the frontier of something you know well? *(getideas)*
- What would be valuable if only it weren't so hard? *(schlep, ambitious)*

---

## F2. Founder tests  *(founders, determination, relres, persistence, earnest, mean, fn, prepare, startupmistakes)*

Ask for **evidence from behavior**, not self-description.

| Quality | Probe | Good evidence |
|---|---|---|
| **Determination** | Tell me about the hardest thing you pushed through when you wanted to quit. | A concrete story with an obstacle that didn't stop them. |
| **Relentless resourcefulness** | When you needed X and had no obvious way to get it, what did you do? | Creative workaround, cold outreach, built it themselves. |
| **Persistent, not obstinate** | What's something you changed your mind about in this project? What criticism have you gotten that you agree with? | Specific mind changes about *means* while holding the *goal*. |
| **Flexibility** | If your current approach proved wrong tomorrow, what would you do? | Several fallbacks, and no panic. |
| **Imagination** | What do you believe about this space that most people don't? | Non-obvious and well reasoned. |
| **Naughtiness** | What rules have you broken (harmlessly) to get something done? | A hacker's disregard for rules that don't matter. |
| **Friendship / cofounders** | Who are your cofounders? How long have you worked together on actual projects? | Long history of building together; a single founder is a flag. |
| **Earnestness** | Why this, really? | Real reasons; little posturing about trends or status. |
| **Builder's habit** | What have you built in the past year, outside any requirement? | Projects, shipped things, side projects. |
| **User empathy** | Describe your user's day. What did you learn from users that surprised you? | Specific, observed details, not guesses. |
| **Not mean** | How do you treat users, cofounders, and competitors? | Generous, not combative. |

---

## F3. Making it powerful  *(powerful)*

Run these once the core idea has some pull. For each, ask whether it would make things
**better for the customer**. If not, discard it.

1. Could you **own the customer relationship** instead of being a component supplier?
2. Could **money (or tokens) flow through you**?
3. Could others **build on you**: an app store, extensions, an **API**, or the standard everyone adopts? (Agents are users now.)
4. Where could **network effects** come from? Can you generalize the idea, let users opt in to sharing, or become a marketplace?
5. Could you **go full stack**, doing the job yourself instead of selling tools to whoever does it? Or take over the customer's hardest work one piece at a time?
6. Is there a **tail that could wag the dog**: a side feature or "misuse" that's the real product?
7. Does it **help users make money**?
8. Could you sell to customers **earlier in their life** (startups, small teams) and grow with them? Who decides **fastest**?
9. Could you get **upstream**: first in the data's life, the money's path, the user's relationship?
10. Are you in a **mafia market** (record labels, PBMs) where the best product doesn't win? If so, how could you come in from the side?
11. What **long-game** trade-off is underpriced because competitors think in quarters?
12. Where are you **cowering**? What's the "you don't need x, just y" simplification?
13. Run it backward: in the customer's perfect world, which piece could you become?

---

## F4. Growth  *(growth, ds, earn, 13sentences)*

- **One metric.** Usually revenue, or active users if it's pre-revenue. It must reflect real value delivered, not vanity numbers.
- **Weekly rate.** 5–7% a week is good, 10% exceptional, around 1% means not there yet. Monthly equivalents: 5%/week ≈ 24%/month and 10%/week ≈ 46%/month.
- **Compounding check.** Use `pgcalc.py growth` to show what the current rate implies in 1, 2, and 5 years.
- **Do things that don't scale**, as a checklist:
  - [ ] Recruited the first users by hand (named people, not ads)
  - [ ] Personally onboarded users, watched them use the product, fixed things the same day
  - [ ] Doing part of the "product" manually behind the scenes
  - [ ] Picked a narrow starting market, small enough to dominate
  - [ ] Customer service that surprises people
  - [ ] Considered consulting for one big first user and building to fit them
- **Word of mouth** is the real test. Are users telling friends? How do you know?

---

## F5. Survival math  *(aord, pinch, ramenprofitable, die)*

- **Default alive?** Assume expenses stay constant and revenue keeps growing at its recent rate. Do you reach profitability before the cash runs out? Run `pgcalc.py alive`.
- **Fatal pinch signs:** several months of runway, high burn, flat or slow growth, and a plan that depends on raising.
- **If default dead:** cut burn now, chase revenue now, and get to ramen profitability. Don't assume a round will come.
- **Ramen profitable:** monthly revenue at least equals the founders' living costs. Track the gap.

---

## F6. Fundraising  *(fr, convince, herd, fundraising, equity, guidetoinvestors, control, corpdev, startupfunding)*

**Readiness (be honest):**
1. Do you need to raise? What would the money *do*? Could you get to ramen profitability instead?
2. Is the company doing well? Fundraising trouble usually signals company trouble.
3. Can you explain it in one sentence, plus why you'll win, plus evidence of growth?
4. Are you formidable, with an opportunity that's genuinely promising? Make it so *before* raising.

**Process:**
- Be in fundraising mode or not, and keep it short.
- Get warm introductions and run investors in parallel (breadth-first, weighted by expected value).
- Hear no until you hear yes. Track where you stand with each investor.
- Get the first commitment, then close committed money immediately.
- Avoid investors who won't lead or who say "keep us posted."
- Ask for less than you think, and keep the next step in mind.
- Equity test: a trade of n of the company is worth it if the company becomes more than 1/(1−n) as valuable. Run `pgcalc.py equity`.
- Keep board control if you can. Don't talk to corp dev unless you want to sell now.
- Keep building during the raise; the company has to keep improving.

---

## F7. The Company Memo  *(what "structuring an idea into a true company" means here)*

A one-page, plain-English document. Each section must be specific enough that someone else
could act on it. Template:

```
# <Company name> — <one plain sentence: what it does, for whom>

## The problem, from the user's point of view
<Who exactly. What they do today. Why it hurts. Observed, not guessed.>

## Why us
<Organic origin. Unusual knowledge. What we've already built.>

## The well
<The small group who want this urgently. Names/count. How we'll reach the first 10, by hand.>

## Version 1
<Smallest thing that is real. What we do manually. Ship date (weeks, not months).>

## The key metric and target growth rate
<One metric. Current value. Weekly target. Where we measure it.>

## What it becomes (the Altair path)
<From toy to big: the sequence of expansions. Why the market grows.>

## What would make it powerful
<1–3 F3 transformations that pass the "better for the customer" test.>

## Money
<How it makes money. Burn. Runway. Default alive? Ramen-profitable target.>

## Risks, ranked
<The one that could kill us first. What we're doing about it this week.>

## This week
<1–3 concrete actions with names and dates. At least one involves talking to users.>
```

---

## F8. The weekly loop  *(users, growth, makersschedule, top)*

Every week:
1. What's the key metric now? What was the rate?
2. Of everything worrying you, **which problem matters most**? (Founders often rank this wrong. Look for the open door, not the cheating boyfriend.)
3. What's one idea to fix it that can be tested **within a week**?
4. What did you learn from users this week?
5. Is anything eating the **top idea in your mind** (fundraising, a dispute, distractions)?
6. Default alive still? Any change?
