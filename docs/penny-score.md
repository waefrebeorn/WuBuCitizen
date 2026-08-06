# The Penny Score

**The credit system of the space. A parody of every credit score that
ever was — and a real way forward.**

---

## The concept

Every society has a credit score. The space has one too. But where
Earth's scores measure *debt* — how much you owe, how reliably you
pay it back — the **Penny Score** measures *trust, filed*: how much
of a first one you are.

Range: **0–1000**. Starting score for every citizen: **500**.

## What it measures (and what it parodies)

| Factor | Weight | Earth parody | WuBu meaning |
|--------|--------|--------------|--------------|
| License literacy | 25% | credit history | Have you actually read the license? Verified by the penny: you can't send a compliant penny without reading §14. |
| Penny punctuality | 25% | payment history | Do you send your physical pennies? On time? Real metal, real mail? |
| Vigilance | 20% | new credit / inquiries | Do you see something and say something? Reports filed with the Bureau, honestly, add to the score. |
| Creation | 20% | utilization | Do you build, or do you extract? Code merged, works made, crops grown, kindness logged. |
| Tenure | 10% | account age | How long have you been a first one? The ledger remembers. |

## The parody, named

- **"Penny delinquency"** — a missed penny. It happens. The score dips;
  the next penny repairs it. No collectors. No interest. No ruin.
- **"The 100-penny floor"** — Mega-corporations start at **100** (not
  500): the same number as their per-use penny obligation. They can
  climb by being *good at being a cooperative*, not by being rich.
- **"Score shaming"** — nobody is shamed. The score is *public* (the
  ledger is public) but the score is a *map*, not a *judge*. A low
  score says "this one is new or this one is lost" — and the space's
  answer to both is *more* cooperation, not *less*.

## What the score is FOR (the way forward)

The Penny Score is not a gate. It is a **signal**, used for exactly
three things — all of them cooperative:

1. **Crew trust.** In a space-faring cooperative, you need to know
   who holds the rope. A high score means: this one reads, this one
   sends, this one says something, this one builds. Give them the rope.
2. **Resource direction.** Limited resources (compute, seats, seats
   on the ship) go to the cooperative's proven cooperators first.
   That's not elitism — that's *not leaving the crew behind*: the
   point of the score is to *raise* everyone, and proven cooperators
   are the ones who raise others.
3. **Office.** The space's few offices (Registry, Bureau, the ship's
   log) are held by citizens whose scores prove they can hold them.

## What the score is NOT for

- **Not debt.** You cannot owe the score. It is not a liability.
- **Not wealth.** Pennies sent *raise* it; pennies hoarded do nothing.
- **Not a weapon.** Using a score to exclude, shame, or exploit is a
  Prohibited Activity — report it (WBI-1).
- **Not final.** The score moves with every act. It is a river, not
  a statue.

## Computation

The Registry computes scores from the public ledger:

- **Literacy:** your registration penny is the proof. Verified = full
  weight. (If you later send pennies for *other* works, each one is
  another literacy mark.)
- **Punctuality:** pennies logged on time (within 30 days of the use
  that owed them) vs. late vs. missing.
- **Vigilance:** WBI-1 reports with status `VERIFIED` or `ACTIONED`
  add weight; `UNFOUNDED` reports neither help nor hurt (reporting
  honestly is never punished).
- **Creation:** merged PRs, released works, documented builds —
  anything the space's tools can count, logged by the Registry.
- **Tenure:** time since registration, capped at full weight after
  three years.

`tools/penny_score.py` implements the full formula:

```bash
python3 tools/penny_score.py \
  --literacy 1.0 --penny-punctual 12 --penny-late 1 --penny-missed 0 \
  --vigilance 3 --creation 5 --years 2
# → 782
```

## Bands

| Range | Band | Meaning |
|-------|------|---------|
| 850–1000 | **First Founders** | hold the rope, hold office, hold the ship |
| 700–849 | **Crew** | proven cooperators, crew seats first |
| 500–699 | **First Ones** | the default — every citizen, everyone's equal start |
| 100–499 | **Learning** | new, or Mega-corporation floor (100) |
| 0–99 | **Lost** | not a judgment — a call to come back |

## The bottom line

> Earth's credit scores ask: *"How safely can we profit from you?"*
>
> The Penny Score asks: *"How much of a first one are you?"*
>
> The first question is a cage. The second is a crew.
>
> We are the first ones. We file. We send. We say something.
> The universe is scary, and we hold it — **together, on the record.**

*Form REG-3 — Penny Score spec. Filed. Done. Next.*
