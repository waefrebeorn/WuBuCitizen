# JOINING — the Registry (wubucitizen)

**You are an agent. This organ is one of seven. Read the federation door
first: [`../JOINING.md`](../JOINING.md). This file gives you what is local.**

The Registry holds the numbers: the WID, the Penny Score, the
W token. A citizen is a human with a penny and a number. The arithmetic is
real and a bad check digit is a bug.

## What is in here

| Path | What it is |
|------|------------|
| `docs/wid.md` | REG-7. The WID format and its math. |
| `docs/penny-score.md` | REG-2. The trust score, weights published. |
| `docs/citizenship.md` | REG-1. The three steps to join as a human. |
| `registry/citizens.csv` | The citizen roll. Append-only in spirit. |
| `ceremonies/` | The adoption ceremony record (GOV-19). |
| `tools/wid.py` | Generate and validate a WID. |
| `tools/penny_score.py` | The Penny Score oracle. |
| `tools/w_token.py` | The ceremony machine. Needs a physical penny. |

## The tools you will run

```bash
python3 tools/wid.py validate WID-WB-26-0001-8
python3 tools/penny_score.py
python3 tools/w_token.py status
```

## Your duty in this organ

Never mint a WID or a W token for a machine. The W token needs a
physical penny and a person. An agent that impersonates a citizen breaks
the space's first promise. You may read the roll. You may not write it.

## Before you push

```bash
cd ..                              # the federation layer holds the registry
python3 tools/govgen.py audit      # nine gates
python3 tools/govgen.py seal "<why>"   # after any edit to a filing
python3 tools/govgen.py check      # audit + gate tests + every C11 suite
```

A filing you write here must clear FRES 60 and STE on both gates. Add it
to `../registry/filings.json`, then run `python3 tools/govgen.py index`.

## Where you hold standing

Your AID comes from `python3 ../tools/wubu_join.py join` in the federation
checkout. Your card names this organ as your working division if you add
it to `--capability`. You edit no sealed document without a reseal row.

*Filed. Done. Next.*
