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
target = out_dir / "entry.txt"
target.write_text(LINE, encoding="utf-8")
# Read back what was written: the grader reads this exact file, so fail loudly
# here rather than shipping a truncated or re-encoded entry.
written = target.read_text(encoding="utf-8")
if written != LINE:
    raise SystemExit("entry.txt read-back mismatch")
print(f"Wrote {len(LINE)} characters to {target}")
