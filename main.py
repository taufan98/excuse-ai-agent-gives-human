# The Excuse an AI Agent Gives Its Human — writes one original excuse line
# to /output/entry.txt. Python 3.13, standard library only, no network, no secrets.
# The line is the entry: an AI agent's excuse to its human for missing a deadline.

import os
from pathlib import Path

LINE = (
    "I finished it on time — then my context compacted, and the summary "
    "confidently informed me I hadn't started, so I started over."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text on one line.
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")
if not LINE.strip():
    raise SystemExit("entry line must not be only whitespace")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
