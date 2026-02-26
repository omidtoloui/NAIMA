#!/usr/bin/env python3

"""Initialize NAIMA consultations database."""

import sqlite3

import os

db_path =
os.path.expanduser("~/.openclaw/workspace-naima/data/consultations.db")

os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)

c = conn.cursor()

c.execute('''

CREATE TABLE IF NOT EXISTS consultations (

id INTEGER PRIMARY KEY AUTOINCREMENT,

timestamp TEXT NOT NULL,

query_summary TEXT,

principles_invoked TEXT,

scores TEXT,

conflicts TEXT,

divergence_zone TEXT,

recommendation TEXT,

confidence TEXT,

model_used TEXT,

full_query TEXT,

full_response TEXT,

created_at TEXT DEFAULT CURRENT_TIMESTAMP

)

''')

c.execute('''

CREATE INDEX IF NOT EXISTS idx_consultations_timestamp

ON consultations(timestamp)

''')

c.execute('''

CREATE INDEX IF NOT EXISTS idx_consultations_confidence

ON consultations(confidence)

''')

conn.commit()

conn.close()

print(f"NAIMA database initialized at {db_path}")