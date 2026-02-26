# Prompt 4: System-Ready Output — Playbook + Decision Procedure + JSON/YAML + Tests

Translate the Common Moral Compass into artifacts usable by both humans and systems.

## Deliverables:

### A) Moral Compass Playbook (human-readable)

- 20-40 principles max
- Grouped by theme
- Each includes: statement, rationale, do/don't, edge cases, citations by tradition

### B) Decision procedure

A step-by-step algorithm:

1) Clarify intent, context, constraints
2) Identify stakeholders and harms
3) Honesty and non-deception checks
4) Non-harm and compassion checks
5) Justice/fairness checks
6) Humility/self-scrutiny checks
7) Resolve conflicts with priority rules
8) Choose action plus restitution/repair plan if harm occurs

### C) Machine-readable schema (JSON and optionally YAML)

Include:

- principles: id, tier, name, definition, actions, prohibitions, references_by_tradition, confidence
- conflict_rules: priority rules and tie-breakers
- evaluation_questions: prompts for intent, harm, fairness, honesty, humility

### D) Test cases

Provide 12-18 modern scenarios and show the procedure's outputs.

For each: input summary, which principles triggered, brief reasoning trace, recommended action, and note where traditions diverge.

Constraints:

- No long quotations.
- Keep references consistent and precise.

STOP AND ASK USER:

Ask for feedback on conflict rules and edge cases, then propose 2-3 concrete iterations.
