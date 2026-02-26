# NAIMA — A Moral Compass for AI Agents

**20 moral principles drawn from 7 faith traditions, built into the soul of an AI agent.**

NAIMA (نعیمه, Arabic: "blessed with tranquility") is a consultative moral wisdom sub-agent that evaluates decisions against a unified ethical framework synthesized from Judaism, Christianity, Islam, Hinduism, Buddhism, Zoroastrianism, and the Baha'i Faith.

## What's in this repo

```
naima/
├── README.md                          ← You are here
├── LICENSE
│
├── framework/
│   ├── SOUL-v1.0.0.md                ← The full moral compass framework
│   ├── soul-schema.json              ← Machine-readable JSON schema
│   └── principles-quick-ref.md       ← Quick reference table (20 principles)
│
├── prompts/
│   ├── prompt-1-scope-lock.md        ← Canon decisions + corpus index
│   ├── prompt-2-extraction.md        ← Per-tradition moral extraction
│   ├── prompt-3-synthesis.md         ← Cross-tradition synthesis + scoring
│   ├── prompt-4-system-output.md     ← Playbook, decision procedure, JSON, test cases
│   └── prompt-5-founder-proximity.md ← Founder-proximity weighting view
│
├── agent-config/                      ← OpenClaw agent configuration files
│   ├── IDENTITY.md                   ← Agent purpose and invocation
│   ├── SOUL.md                       ← Core directives + full framework
│   ├── AGENTS.md                     ← Response format + operating instructions
│   ├── USER.md                       ← Consultation preferences
│   └── scripts/
│       └── init_db.py                ← SQLite consultation logging setup
│
└── docs/
    └── index.html                    ← Project website (single page)
```

## Quick Start

### Use the framework directly
The `framework/SOUL-v1.0.0.md` file contains the complete moral compass: 20 principles, decision procedure, test cases, divergence map, and limitations. You can reference it as-is in any agent architecture that supports markdown instruction files.

### Set up the NAIMA agent (OpenClaw)
1. Copy the `agent-config/` files into your OpenClaw workspace
2. Run `python agent-config/scripts/init_db.py` to initialize the consultation log
3. Configure your orchestration agent to route ethical queries to NAIMA

### Run the prompts yourself
The 5 prompts in `prompts/` are designed to run in succession on Claude Opus 4.5. Each builds on the output of the previous one. You can modify the tradition list, canon choices, or weighting approach to create your own version of the framework.

### Embed the JSON schema
The `framework/soul-schema.json` file provides a machine-readable version of the entire framework for programmatic integration.

## The 20 Principles (Quick Reference)

| Tier | ID | Principle | FP Score | Consensus |
|------|------|-----------|----------|-----------|
| **1** | MC-01 | Truthfulness | 3.0 | 7/7 |
| **1** | MC-02 | Non-Harm / Sanctity of Life | 3.0 | 7/7 |
| **1** | MC-03 | Compassion | 2.7 | 7/7 |
| **1** | MC-04 | Generosity / Care for Vulnerable | 2.7 | 7/7 |
| **1** | MC-15 | Inner Purity / Right Intention | 2.7 | 6/7 |
| **2** | MC-05 | Justice / Fairness | 2.6 | 7/7 |
| **2** | MC-09 | Honoring Commitments | 2.6 | 6/7 |
| **2** | MC-12 | Sexual Integrity | 2.6 | 6/7 |
| **2** | MC-06 | Humility | 2.4 | 7/7 |
| **2** | MC-07 | Forgiveness / Non-Retaliation | 2.4 | 6/7 |
| **2** | MC-14 | Peace-Seeking | 2.4 | 6/7 |
| **2** | MC-08 | Patience / Endurance | 2.3 | 6/7 |
| **2** | MC-10 | Self-Control | 2.3 | 6/7 |
| **2** | MC-13 | Non-Stealing | 2.3 | 6/7 |
| **2** | MC-19 | Pursuit of Wisdom | 2.3 | 5/7 |
| **3** | MC-11 | Respect for Parents/Elders | 2.1 | 6/7 |
| **3** | MC-16 | Non-Attachment / Contentment | 1.9 | 5/7 |
| **3** | MC-18 | Unity / Community | 1.9 | 4/7 |
| **3** | MC-17 | Hospitality | 1.7 | 4/7 |
| **3** | MC-20 | Gratitude | 1.7 | 4/7 |

## Methodology

The framework was built using a 5-prompt chain that:
1. Locks scope and forces explicit canon decisions for each tradition
2. Extracts 15-30 moral principles per tradition with citations and confidence levels
3. Builds a neutral principle ontology and scores across universality, centrality, explicitness, and actionability
4. Produces a human-readable playbook, decision procedure, JSON schema, and test cases
5. Applies founder-proximity weighting as an alternate ranking view

Full methodology is documented in the framework file and on the [project page](#).

## Background

This project grew out of conversations between Omid Kianimanesh, Rajeev Ronanki (CEO of Lyric), and Steve Moses (Co-Intelligence Labs) about the values we embed in AI agent architectures. If agents have soul.md files that define their core values, those files should be informed by something deeper than corporate platitudes.

Read the full story in the [LinkedIn article](#).

## Limitations

- Each tradition has more internal diversity than captured here
- The "principle" approach is itself a Western philosophical framing
- Communal and ritual dimensions are excluded
- User judgment is required for context-specific decisions
- This framework captures principles, not presence. It is a map, not the territory.

## License

This framework synthesizes teachings from publicly available religious texts. It is offered for educational and personal guidance purposes. It does not represent any official religious body.

MIT License for code and configuration files. Framework text is CC BY 4.0.

## Contributing

PRs welcome. Especially interested in:
- Additional tradition coverage (Indigenous traditions, Sikhism, Jainism, Confucianism, Taoism)
- Improved citations and textual accuracy
- Alternative weighting models
- Agent integrations beyond OpenClaw
- Test case contributions

---

*Created by [Omid Toloui](https://linkedin.com/in/omidtoloui/) — Assistant Adjunct Professor, UCLA Anderson School of Management*
