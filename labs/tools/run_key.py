"""Run a lab's key against the live sites, in place, one cell at a time.

    LAB_EMAIL=you@colorado.edu python labs/tools/run_key.py labs/week-NN/lab-NN-key.ipynb

Every code cell runs once, in order, in one kernel, from a scratch folder, so
files a lab downloads stay out of the repository. A cell that fails with a
rate limit or a dropped connection is rerun after a pause, up to --retries
times. A cell that still fails keeps its code, loses its outputs, and is
tagged "not-run-live" and "skip-execution"; the run goes on, and the report at
the end lists those cells for the pull request. Cells already tagged
"skip-execution" (an optional step) are left alone.

Before running, your-email@colorado.edu becomes LAB_EMAIL; afterwards it goes
back, in code and outputs. The notebook isn't written if an output contains
the value of an environment variable whose name ends in _KEY, _TOKEN, or
_SECRET. See labs/AUTHORING.md.
"""
import argparse
import os
import re
import sys
import tempfile
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

PLACEHOLDER = "your-email@colorado.edu"
ANSI = re.compile(r"\x1b\[[0-9;]*m")
TRANSIENT = re.compile(r"\b(429|502|503|504)\b|Too Many Requests|timed? ?out|ConnectionError|"
                       r"RemoteDisconnected|Connection reset|Max retries exceeded")


def swap(nb, old, new):
    for cell in nb.cells:
        cell.source = cell.source.replace(old, new)
        for output in cell.get("outputs", []):
            if "text" in output:
                output.text = output.text.replace(old, new)
            for kind, value in output.get("data", {}).items():
                if kind.startswith("text/") and isinstance(value, str):
                    output.data[kind] = value.replace(old, new)


def secrets():
    return {name: value for name, value in os.environ.items()
            if re.search(r"_(KEY|TOKEN|SECRET)$", name) and len(value) >= 8}


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("key", type=Path)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--wait", type=int, default=90, help="seconds between tries")
    args = parser.parse_args()
    email = os.environ.get("LAB_EMAIL")
    if not email:
        sys.exit("set LAB_EMAIL to the address the User-Agent should carry")

    nb = nbformat.read(args.key, as_version=4)
    swap(nb, PLACEHOLDER, email)
    not_run = []
    with tempfile.TemporaryDirectory() as scratch:
        client = NotebookClient(nb, timeout=1200, kernel_name="python3", record_timing=False,
                                resources={"metadata": {"path": scratch}})
        with client.setup_kernel():
            for index, cell in enumerate(nb.cells):
                if cell.cell_type != "code":
                    continue
                cell.metadata.pop("execution", None)
                tags = cell.metadata.setdefault("tags", [])
                if "not-run-live" in tags:      # left from an earlier run: try again
                    tags.remove("not-run-live")
                    tags.remove("skip-execution")
                if "skip-execution" in tags:
                    continue
                for attempt in range(args.retries + 1):
                    try:
                        client.execute_cell(cell, index)
                        break
                    except CellExecutionError as error:
                        message = ANSI.sub("", str(error)).strip().splitlines()[-1][:200]
                        if TRANSIENT.search(str(error)) and attempt < args.retries:
                            print(f"cell {index}: {message}; waiting {args.wait} s", flush=True)
                            time.sleep(args.wait)
                            continue
                        print(f"cell {index}: not run live ({message})", flush=True)
                        cell.outputs = []
                        cell.execution_count = None
                        tags.extend(["not-run-live", "skip-execution"])
                        not_run.append((index, message))
                        break
                if not tags:
                    del cell.metadata["tags"]

    swap(nb, email, PLACEHOLDER)
    text = nbformat.writes(nb)
    leaked = [name for name, value in secrets().items() if value in text]
    if leaked:
        sys.exit(f"not written: the notebook contains the value of {', '.join(leaked)}")
    if email in text:
        sys.exit("not written: the notebook still contains LAB_EMAIL")
    args.key.write_text(text)
    print(f"wrote {args.key}")
    if not_run:
        print("Not run live (list these in the pull request):")
        for index, message in not_run:
            print(f"  cell {index}: {message}")


if __name__ == "__main__":
    main()
