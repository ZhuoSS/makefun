"""Write one line of text to entry.txt for the make.fun roast bounty."""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

LINE = (
    "I asked my agent to think outside the box. "
    "It spent four hours building a box, then asked me to think inside it."
)

(OUT_DIR / "entry.txt").write_text(LINE, encoding="utf-8")
