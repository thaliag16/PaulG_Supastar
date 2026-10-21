#!/usr/bin/env python3
"""pgcalc — the arithmetic behind Paul Graham's startup essays.

  alive   Default Alive or Default Dead?   (paulgraham.com/aord.html)
  growth  What a growth rate compounds to   (growth.html, earn.html)
  weekly  Growth rate from a metric series  (growth.html)
  equity  The Equity Equation, 1/(1-n)      (equity.html)
  ramen   Distance to ramen profitability   (ramenprofitable.html)

Stdlib only. All money values are in whatever currency you use; rates are decimals (0.1 = 10%).
"""
import argparse
import math
import sys


def money(x):
    return f"{x:,.0f}"


def cmd_alive(a):
    if a.weekly_growth is not None:
        g = (1 + a.weekly_growth) ** (52 / 12) - 1
    else:
        g = a.growth
    cash, rev, burn = a.cash, a.revenue, a.burn
    print(f"Assumptions: expenses constant at {money(burn)}/mo, revenue {money(rev)}/mo "
          f"growing {g*100:.1f}%/mo, cash {money(cash)}.")
    if rev >= burn:
        print("\nDEFAULT ALIVE: you're already profitable.")
        return
    for month in range(1, a.horizon + 1):
        cash -= burn - rev
        if cash < 0:
            print(f"\nDEFAULT DEAD: cash runs out in month {month} "
                  f"(revenue then {money(rev)}/mo vs expenses {money(burn)}/mo).")
            need = None
            # Smallest monthly growth rate that would make it (bisection).
            lo, hi = 0.0, 3.0
            for _ in range(60):
                mid = (lo + hi) / 2
                if _survives(a.cash, a.revenue, burn, mid, a.horizon):
                    hi = mid
                else:
                    lo = mid
            if _survives(a.cash, a.revenue, burn, hi, a.horizon):
                need = hi
            if need is not None and a.revenue > 0:
                print(f"To be default alive at these expenses you'd need ~{need*100:.1f}%/mo "
                      f"revenue growth (~{((1+need)**(12/52)-1)*100:.1f}%/wk).")
            flat = a.cash / (burn - a.revenue)
            print(f"With zero growth, runway is {flat:.1f} months.")
            print("Read: paulgraham.com/aord.html and paulgraham.com/pinch.html")
            return
        rev *= 1 + g
        if rev >= burn:
            print(f"\nDEFAULT ALIVE: profitable in month {month + 1} with "
                  f"{money(cash)} still in the bank.")
            print("Keep it that way: don't let expenses grow faster than revenue. (aord.html)")
            return
    print(f"\nNot profitable within {a.horizon} months, though cash lasts. Treat as default dead.")


def _survives(cash, rev, burn, g, horizon):
    for _ in range(horizon):
        if rev >= burn:
            return True
        cash -= burn - rev
        if cash < 0:
            return False
        rev *= 1 + g
    return rev >= burn


def cmd_growth(a):
    r = a.rate
    monthly = (1 + r) ** (52 / 12) - 1 if a.period == "week" else r
    weekly = (1 + monthly) ** (12 / 52) - 1
    print(f"{weekly*100:.2f}%/week = {monthly*100:.1f}%/month = "
          f"{((1+monthly)**12)*100-100:,.0f}%/year")
    print("\nBenchmarks (growth.html): ~1%/wk = not there yet, 5-7%/wk = good, 10%/wk = exceptional.\n")
    for months in (3, 6, 12, 24, 36, 60):
        mult = (1 + monthly) ** months
        line = f"  after {months:>2} months: {mult:>14,.1f}x"
        if a.start:
            line += f"   ({money(a.start)} -> {money(a.start*mult)})"
        print(line)
    if a.target:
        months = math.log(a.target) / math.log(1 + monthly)
        print(f"\nTime to grow {a.target:,.0f}x: {months:.2f} months (earn.html does this same math).")


def cmd_weekly(a):
    vals = [float(v) for v in a.values.split(",") if v.strip()]
    if len(vals) < 2:
        sys.exit("Need at least two values, e.g. --values 100,108,117")
    print("Week-over-week:")
    for i in range(1, len(vals)):
        prev, cur = vals[i - 1], vals[i]
        pct = (cur / prev - 1) * 100 if prev else float("inf")
        print(f"  {i:>2}: {prev:,.0f} -> {cur:,.0f}  ({pct:+.1f}%)")
    n = len(vals) - 1
    if vals[0] > 0:
        cagr = (vals[-1] / vals[0]) ** (1 / n) - 1
        verdict = ("exceptional" if cagr >= 0.10 else "good" if cagr >= 0.05
                   else "ok, push harder" if cagr >= 0.02 else "not there yet")
        print(f"\nCompound weekly rate: {cagr*100:.1f}%  -> {verdict} (growth.html)")


def cmd_equity(a):
    n = a.give
    if not 0 < n < 1:
        sys.exit("--give must be a fraction between 0 and 1, e.g. 0.1")
    k = 1 / (1 - n)
    print(f"Giving up {n*100:.1f}% is worth it only if it makes the company more than "
          f"{k:.3f}x as valuable (i.e. +{(k-1)*100:.1f}%).  (equity.html)")
    if a.premoney:
        post = a.premoney / (1 - n)
        print(f"At a {money(a.premoney)} pre-money, that's raising {money(post - a.premoney)} "
              f"at {money(post)} post.")


def cmd_ramen(a):
    gap = a.living - a.revenue
    if gap <= 0:
        print("You're ramen profitable. Investors now need you more than you need them. "
              "(ramenprofitable.html)")
    else:
        print(f"Ramen gap: {money(gap)}/mo ({a.revenue/a.living*100:.0f}% of the way).")
        if a.growth:
            months = math.log(a.living / a.revenue) / math.log(1 + a.growth) if a.revenue > 0 else float("inf")
            print(f"At {a.growth*100:.1f}%/mo revenue growth: ~{months:.1f} months to ramen profitable.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)

    al = s.add_parser("alive", help="default alive or default dead?")
    al.add_argument("--cash", type=float, required=True, help="cash in bank")
    al.add_argument("--burn", type=float, required=True, help="monthly expenses (gross)")
    al.add_argument("--revenue", type=float, required=True, help="current monthly revenue")
    al.add_argument("--growth", type=float, default=0.0, help="monthly revenue growth, e.g. 0.1")
    al.add_argument("--weekly-growth", type=float, help="weekly growth instead of monthly")
    al.add_argument("--horizon", type=int, default=120, help="months to simulate")
    al.set_defaults(f=cmd_alive)

    gr = s.add_parser("growth", help="what a growth rate compounds to")
    gr.add_argument("--rate", type=float, required=True)
    gr.add_argument("--period", choices=["week", "month"], default="week")
    gr.add_argument("--start", type=float, help="current value of the metric")
    gr.add_argument("--target", type=float, help="multiple to reach, e.g. 500")
    gr.set_defaults(f=cmd_growth)

    wk = s.add_parser("weekly", help="growth rate from weekly metric values")
    wk.add_argument("--values", required=True, help="comma-separated, oldest first")
    wk.set_defaults(f=cmd_weekly)

    eq = s.add_parser("equity", help="the equity equation")
    eq.add_argument("--give", type=float, required=True, help="fraction given up, e.g. 0.1")
    eq.add_argument("--premoney", type=float, help="pre-money valuation (optional)")
    eq.set_defaults(f=cmd_equity)

    ra = s.add_parser("ramen", help="distance to ramen profitability")
    ra.add_argument("--revenue", type=float, required=True, help="monthly revenue")
    ra.add_argument("--living", type=float, required=True, help="founders' total monthly living costs")
    ra.add_argument("--growth", type=float, help="monthly revenue growth")
    ra.set_defaults(f=cmd_ramen)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
