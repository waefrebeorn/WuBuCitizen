#!/usr/bin/env python3
"""WID — WuBu IDentification Number (generate & validate).

~ WuBuCitizen ~ the Registry of the First Ones.

Usage:
  wid.py generate <mind-country> <year> <sequence>
      e.g. wid.py generate WB 26 0001  ->  WID-WB-26-0001-8

  wid.py validate <WID>
      e.g. wid.py validate WID-WB-26-0001-8  ->  VALID
"""
import re
import sys

WID_RE = re.compile(r"^WID-([A-Z]{2})-(\d{2})-(\d{4})-([0-9X])$")


def check_digit(yy: str, nnnn: str) -> str:
    """Mod-11 check digit, ISBN-family weights (right-to-left ×2..×7)."""
    digits = [int(c) for c in (yy + nnnn)]
    weights = [7, 6, 5, 4, 3, 2]  # applied left-to-right == right-to-left ×2..×7
    total = sum(d * w for d, w in zip(digits, weights))
    rem = total % 11
    return "X" if rem == 10 else str(rem)


def generate(mind_country: str, year: str, sequence: str) -> str:
    if not re.fullmatch(r"[A-Z]{2}", mind_country):
        raise ValueError(f"mind-country must be 2 uppercase letters, got {mind_country!r}")
    if not re.fullmatch(r"\d{2}", year):
        raise ValueError(f"year must be 2 digits, got {year!r}")
    if not re.fullmatch(r"\d{4}", sequence):
        raise ValueError(f"sequence must be 4 digits, got {sequence!r}")
    c = check_digit(year, sequence)
    return f"WID-{mind_country}-{year}-{sequence}-{c}"


def validate(wid: str) -> tuple[bool, str]:
    m = WID_RE.match(wid)
    if not m:
        return False, "malformed (expected WID-XX-YY-NNNN-C)"
    country, yy, nnnn, given = m.groups()
    expected = check_digit(yy, nnnn)
    if given != expected:
        return False, f"check digit mismatch (expected {expected}, got {given})"
    return True, "valid"


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args[0] == "generate" and len(args) == 4:
        _, country, yy, seq = args
        print(generate(country, yy, seq))
        return 0
    if args[0] == "validate" and len(args) == 2:
        ok, msg = validate(args[1])
        print("VALID" if ok else f"INVALID — {msg}")
        return 0 if ok else 1
    print(__doc__)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
