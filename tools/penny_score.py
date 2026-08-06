#!/usr/bin/env python3
"""penny_score.py — the Penny Score (0-1000) for WuBuCitizen.

~ The Registry of the First Ones ~

Usage:
  penny_score.py [--literacy F] [--penny-punctual N] [--penny-late N]
                 [--penny-missed N] [--vigilance N] [--creation N]
                 [--years Y]

All weights per docs/penny-score.md:
  literacy 25% | punctuality 25% | vigilance 20% | creation 20% | tenure 10%

Example:
  python3 penny_score.py --literacy 1.0 --penny-punctual 12 --penny-late 1 \
      --penny-missed 0 --vigilance 3 --creation 5 --years 2
"""
import argparse


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def compute(literacy, penny_punctual, penny_late, penny_missed,
            vigilance, creation, years):
    # Literacy: 0..1 (registration penny verified = 1.0)
    lit = clamp(literacy)

    # Punctuality: punctual / total pennies owed (on-time + late + missed)
    total = penny_punctual + penny_late + penny_missed
    punct = clamp(penny_punctual / total) if total > 0 else 0.0

    # Vigilance: verified/actioned reports; 5 reports = full weight
    vig = clamp(vigilance / 5)

    # Creation: merged works / releases; 10 works = full weight
    cre = clamp(creation / 10)

    # Tenure: 3 years = full weight
    ten = clamp(years / 3)

    score = (
        lit * 250
        + punct * 250
        + vig * 200
        + cre * 200
        + ten * 100
    )
    return round(score)


def band(score):
    if score >= 850:
        return "First Founders — hold the rope, hold office, hold the ship"
    if score >= 700:
        return "Crew — proven cooperator, crew seats first"
    if score >= 500:
        return "First Ones — the default, everyone's equal start"
    if score >= 100:
        return "Learning — new, or the Mega-corporation floor (100)"
    return "Lost — not a judgment, a call to come back"


def main():
    p = argparse.ArgumentParser(description="Penny Score (0-1000)")
    p.add_argument("--literacy", type=float, default=1.0, help="0..1 (registration penny verified = 1.0)")
    p.add_argument("--penny-punctual", type=int, default=1)
    p.add_argument("--penny-late", type=int, default=0)
    p.add_argument("--penny-missed", type=int, default=0)
    p.add_argument("--vigilance", type=int, default=0, help="verified/actioned WBI-1 reports")
    p.add_argument("--creation", type=int, default=0, help="merged works / releases")
    p.add_argument("--years", type=float, default=0.0, help="years since registration")
    args = p.parse_args()

    score = compute(args.literacy, args.penny_punctual, args.penny_late,
                    args.penny_missed, args.vigilance, args.creation, args.years)
    print(f"Penny Score: {score}/1000")
    print(f"Band:        {band(score)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
