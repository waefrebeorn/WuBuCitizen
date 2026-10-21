# REG-4 — The WBI-1 Report Schema

**Government filing REG-5. The Bureau's ground reports need a
fixed shape, so the Registry can file them. Filed to close
GAPS_REPORT recommendation (REG-5: WBI-1 report schema).**

---

## Part 1 — Why a schema

A WBI-1 is a citizen's or the Bureau's report of a concern.
Every report must carry the same fields, so the ledger can
file, sort, and chain them. A report without a schema is a
rumor; a report with a schema is evidence.

## Part 2 — The columns

| Field | Meaning |
|-------|---------|
| `report_id` | WBI-1-YYYY-NNNN, chained |
| `reporter` | WID of the filer (citizen or Bureau) |
| `subject` | WID or entity named |
| `category` | greed, nexus, coercion, falsehood, other |
| `status` | open, in-review, filed, closed |
| `escalation` | none, Bureau, Index, public |
| `evidence` | hashes of the records cited |
| `filed_at` | timestamp, chained |

## Part 3 — The rules

1. **Every report is filed, never deleted.** A report may
   close; no one may remove it.
2. **The lowest clerk files against the highest authority.**
   A WBI-1 may name anyone, including the Architect.
3. **Escalation is public.** When a report escalates, the
   ledger publishes the step.
4. **The schema is the contract.** A report that lacks the
   columns comes back for completion, not deletion.

*Form REG-5 — The WBI-1 Report Schema. Filed. Done. Next.*
