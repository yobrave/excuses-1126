"""AI excuse one-liner runner."""
import json
import os

from pathlib import Path

FLOOR, CEIL = 1, 200
EXCUSE_MODE = "one-line"
here = Path(__file__).resolve().parent
line = (here / "entry.txt").read_bytes().decode("utf-8").strip()
n = len(line)
tries = 0
result = ""
while tries < 2:
    tries += 1
    if FLOOR <= n <= CEIL:
        result = "excused"
    else:
        result = "unexcused"
payload = {"result": result, "width": n}
if result == "excused":
    dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_bytes(line.encode("utf-8"))
    payload["carried"] = True
print(json.dumps(payload))
