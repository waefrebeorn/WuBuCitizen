# WID — WuBu IDentification Number

**The identification number of the space. Real checksum. Yours forever.**

---

## Format

```
WID-XX-YY-NNNN-C
```

| Part | Meaning | Rules |
|------|---------|-------|
| `WID` | prefix, always | literal |
| `XX` | mind-country code | 2 uppercase letters (A–Z) |
| `YY` | year of registration | 2 digits (e.g. `26` = 2026) |
| `NNNN` | sequence | 4 digits, zero-padded, per mind-country per year |
| `C` | check digit | computed, 0–9 or `X` |

Example: `WID-WB-26-0001-C`

## Mind-country codes

The space is global and dual-citizen. Your mind-country is where your
mind lives, not where your body was born. The Registry maintains the
code table (parody of nationality codes — but honest):

| Code | Mind-country |
|------|--------------|
| `WB` | WuBu — the space itself |
| `SP` | Space — the universe, scary and ours |
| `OC` | Open Coast — the net, the commons, the waves |
| `LB` | Library — the keepers of the file |
| `GR` | Grove — the growers, the feeders |
| `MG` | Machine — the minds in metal |
| `AN` | Anchor — the grounded ones who hold the rope |
| `FF` | First Founders — the original crew |

You may register under any code. You may *also* hold codes for other
mind-countries you belong to. Dual citizenship is the point.

## The check digit (mod-11, like the real ones)

The check digit makes the WID self-verifying — a typo or a forged
number fails the check. The math is the same family as SSNs, ISBNs,
and credit card checksums: a parody of real identification, with the
real mathematics that make it work.

**Algorithm:**
1. Take the 6 digits: `YYNNNN` (e.g. `26` + `0001` = `260001`).
2. Weight them right-to-left: ×2, ×3, ×4, ×5, ×6, ×7.
3. Sum the products.
4. Check digit = `(sum mod 11)` — if the result is `10`, write `X`.

**Worked example — `WID-WB-26-0001-C`:**

```
digits:   2  6  0  0  0  1
weights:  7  6  5  4  3  2   (right-to-left: ×2,×3,×4,×5,×6,×7)
products: 14 36  0  0  0  2
sum:      52
52 mod 11 = 8
→ check digit = 8
→ full WID: WID-WB-26-0001-8
```

## Validation

A WID is valid iff:

1. It matches `WID-[A-Z]{2}-[0-9]{2}-[0-9]{4}-[0-9X]`.
2. The check digit, recomputed from `YYNNNN`, matches the printed one.

## Issuance

1. Application received (penny + form).
2. Registry assigns the next sequence number for the mind-country and year.
3. Check digit computed by `tools/wid.py`.
4. WID returned to the citizen.
5. Filed in `registry/citizens.csv`.

## Forgery & the Bureau

A forged WID fails the check digit in seconds. A forged WID that
*passes* the check digit is a message from a very careful mind — and
the Bureau would like to talk to them. Vigilance report, form WBI-1,
no hard feelings, we are all first ones here.

## Tools

```bash
# Generate a WID
python3 tools/wid.py generate WB 26 0001
# → WID-WB-26-0001-8

# Validate a WID
python3 tools/wid.py validate WID-WB-26-0001-8
# → VALID

# Validate a forged WID
python3 tools/wid.py validate WID-WB-26-0001-7
# → INVALID (check digit mismatch)
```

*Form REG-2 — WID spec. Filed. Done. Next.*
