#!/usr/bin/env python3
"""w_token.py — the WuBu W Token ceremony machine.

GOV-19 / GOV-30 / RND-24 / RND-42. The ceremony turns an old
penny into a token of trust. The plastic token system handles
assets and agreements.

Commands:
  w_token ceremony <wid>              — run the W Token ceremony
  w_token mint_plastic <wid> <desc>   — mint a plastic token
  w_token status                      — show token counts
  w_token verify <serial>             — verify a token

One-stamp rule: one metal token per human, never reprinted.
Plastic tokens: reprintable, ledger survives loss.
"""

import hashlib
import json
import os
import sys
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "tokens")
os.makedirs(DATA, exist_ok=True)

METAL_FILE = os.path.join(DATA, "metal_tokens.json")
PLASTIC_FILE = os.path.join(DATA, "plastic_tokens.json")
LEDGER_FILE = os.path.join(DATA, "w_token_ledger.json")
CEREMONIES = os.path.join(DATA, "ceremonies")
os.makedirs(CEREMONIES, exist_ok=True)

PENNY_COPPER = 3.11
PENNY_ZINC = 2.50


def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()


def chain_hash(prev, entry):
    return sha256(prev + json.dumps(entry, sort_keys=True))


def ceremony(wid):
    """Run the W Token ceremony. One per human. Never reprinted."""
    metal = load_json(METAL_FILE, {"tokens": [], "count": 0})
    ledger = load_json(LEDGER_FILE, {"chain": [], "root": "GENESIS"})

    # Check if this WID already has a metal token
    for t in metal["tokens"]:
        if t["wid"] == wid:
            print(f"ERROR: {wid} already has metal token {t['serial']}")
            print("One-stamp rule: one per human. Never reprinted.")
            return None

    # Weigh the penny
    print("=" * 50)
    print("W TOKEN CEREMONY")
    print("=" * 50)
    print(f"\nCitizen: {wid}")
    print("Place the penny on the scale.")
    weight = float(input("Enter penny weight (g): ").strip())

    # Classify
    if abs(weight - PENNY_COPPER) < 0.1:
        penny_class = "copper"
        print(f"Copper penny ({PENNY_COPPER}g) confirmed.")
    elif abs(weight - PENNY_ZINC) < 0.1:
        penny_class = "zinc"
        print(f"Zinc penny ({PENNY_ZINC}g) confirmed.")
    else:
        print(f"WARNING: {weight}g is not a standard penny.")
        confirm = input("Proceed anyway? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Ceremony aborted.")
            return None
        penny_class = "unknown"

    # One-stamp rule
    metal["count"] += 1
    ordinal = metal["count"]
    serial = f"WT-{wid}-{ordinal:04d}"

    # Chain hash
    prev_hash = ledger["chain"][-1]["hash"] if ledger["chain"] else "GENESIS"
    entry = {
        "serial": serial,
        "wid": wid,
        "type": "metal",
        "penny_class": penny_class,
        "weight": weight,
        "timestamp": time.time()
    }
    h = chain_hash(prev_hash, entry)
    entry["hash"] = h

    # Mint
    token = {
        "serial": serial,
        "wid": wid,
        "penny_class": penny_class,
        "weight": weight,
        "hash": h,
        "timestamp": entry["timestamp"],
        "ceremony_record": f"ceremony-{wid}-{ordinal}.md"
    }
    metal["tokens"].append(token)
    ledger["chain"].append(entry)

    # Ceremony record
    ceremony_file = os.path.join(CEREMONIES, f"ceremony-{wid}-{ordinal}.md")
    with open(ceremony_file, 'w') as f:
        f.write(f"# W Token Ceremony — {wid}\n\n")
        f.write(f"**Ordinal:** {ordinal}\n")
        f.write(f"**Serial:** {serial}\n")
        f.write(f"**Penny class:** {penny_class}\n")
        f.write(f"**Weight:** {weight}g\n")
        f.write(f"**Hash:** {h[:32]}...\n\n")
        f.write("This ceremony was a feeling-special moment.\n")
        f.write("It exists so the person feels special.\n")
        f.write("That is its whole job.\n\n")
        f.write("The room applauded.\n")
        f.write("Witnesses gave gifts toward the citizen's start.\n")
        f.write("The space files this moment forever.\n\n")
        f.write(f"*Filed. Done. Next.*\n")

    save_json(METAL_FILE, metal)
    save_json(LEDGER_FILE, ledger)

    print(f"\n{'=' * 50}")
    print(f"TOKEN MINTED: {serial}")
    print(f"Penny class: {penny_class}")
    print(f"Weight: {weight}g")
    print(f"Hash: {h[:32]}...")
    print(f"Ceremony record: {ceremony_file}")
    print(f"{'=' * 50}")
    print("\nThe penny is no longer money.")
    print("It is now a token of humanity.")
    print("It is societal credit the person owns for life.")
    return serial


def mint_plastic(wid, description):
    """Mint a plastic token. Reprintable."""
    plastic = load_json(PLASTIC_FILE, {"tokens": [], "count": 0})
    ledger = load_json(LEDGER_FILE, {"chain": [], "root": "GENESIS"})

    plastic["count"] += 1
    ordinal = plastic["count"]
    serial = f"PL-{wid}-{ordinal:04d}"

    prev_hash = ledger["chain"][-1]["hash"] if ledger["chain"] else "GENESIS"
    entry = {
        "serial": serial,
        "wid": wid,
        "type": "plastic",
        "description": description,
        "timestamp": time.time()
    }
    h = chain_hash(prev_hash, entry)
    entry["hash"] = h

    token = {
        "serial": serial,
        "wid": wid,
        "description": description,
        "hash": h,
        "timestamp": entry["timestamp"]
    }
    plastic["tokens"].append(token)
    ledger["chain"].append(entry)

    save_json(PLASTIC_FILE, plastic)
    save_json(LEDGER_FILE, ledger)

    print(f"Minted plastic token: {serial}")
    print(f"Description: {description}")
    print(f"Hash: {h[:32]}...")
    return serial


def status():
    metal = load_json(METAL_FILE, {"tokens": [], "count": 0})
    plastic = load_json(PLASTIC_FILE, {"tokens": [], "count": 0})
    ledger = load_json(LEDGER_FILE, {"chain": []})

    print("=" * 50)
    print("W TOKEN SYSTEM — STATUS")
    print("=" * 50)
    print(f"\nMetal tokens: {metal['count']} (one per human, never reprinted)")
    print(f"Plastic tokens: {plastic['count']} (reprintable)")
    print(f"Ledger entries: {len(ledger['chain'])}")

    if metal["tokens"]:
        print("\nMetal tokens:")
        for t in metal["tokens"][-5:]:
            print(f"  {t['serial']} — {t['penny_class']} ({t['weight']}g)")
        if len(metal["tokens"]) > 5:
            print(f"  ... and {len(metal['tokens']) - 5} more")

    if plastic["tokens"]:
        print("\nPlastic tokens (last 5):")
        for t in plastic["tokens"][-5:]:
            print(f"  {t['serial']} — {t['description'][:40]}...")
        if len(plastic["tokens"]) > 5:
            print(f"  ... and {len(plastic['tokens']) - 5} more")


def verify(serial):
    """Verify a token's hash against the ledger."""
    ledger = load_json(LEDGER_FILE, {"chain": []})
    for entry in ledger["chain"]:
        if entry["serial"] == serial:
            print(f"TOKEN FOUND: {serial}")
            print(f"Type: {entry['type']}")
            print(f"WID: {entry['wid']}")
            if entry['type'] == 'metal':
                print(f"Penny class: {entry['penny_class']}")
                print(f"Weight: {entry['weight']}g")
            else:
                print(f"Description: {entry['description']}")
            print(f"Hash: {entry['hash'][:32]}...")
            print("Status: VERIFIED")
            return True
    print(f"Token {serial} not found.")
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: w_token <ceremony|mint_plastic|status|verify> [args]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "ceremony" and len(sys.argv) >= 3:
        ceremony(sys.argv[2])
    elif cmd == "mint_plastic" and len(sys.argv) >= 4:
        mint_plastic(sys.argv[2], " ".join(sys.argv[3:]))
    elif cmd == "status":
        status()
    elif cmd == "verify" and len(sys.argv) >= 3:
        verify(sys.argv[2])
    else:
        print("Unknown command or missing arguments")
        sys.exit(1)
