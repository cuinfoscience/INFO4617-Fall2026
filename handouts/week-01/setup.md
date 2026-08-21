# Getting set up

*Do this before Monday, August 24 — INFO 4617 Web Data Science*

Three things need to work on your own laptop before the first notebook lab.
Budget about 45 minutes. **If you get stuck, email me before Monday** rather
than arriving without a working environment —
[brian.keegan@colorado.edu](mailto:brian.keegan@colorado.edu).

| | What | Why |
|---|---|---|
| 1 | **Python, via Anaconda** | The language plus a curated scientific stack and the `conda` package manager |
| 2 | **GitHub Desktop or the `gh` CLI** | Get changes from your laptop into a pull request — no command-line `git` required |
| 3 | **A free GitHub account** | Where the textbook lives and where you submit revisions |

---

## 1 · Python via Anaconda

Install Anaconda from [anaconda.com](https://www.anaconda.com/download), then
give this course its own isolated environment:

```bash
conda create -n webdata python=3.11
conda activate webdata
pip install requests beautifulsoup4 pandas matplotlib seaborn
```

One environment per project records **exactly** which versions your analysis ran
against. That's reproducibility, not just tidiness — and it keeps this course
from breaking another project's dependencies.

Launch your workspace with:

```bash
jupyter notebook
```

Jupyter opens in your browser and puts code, notes, and results in one file.

![Anaconda launches Jupyter in your browser](../slides/week-01/img/anaconda_jupyter.png)

> **Note:** coursework is done in Python. Spreadsheet and BI tools (Excel,
> Tableau, Power BI) are not used for assignments.

### Check that it worked

Make a new notebook and run this. Retrieving a web page programmatically is one
call:

```python
import requests

url = "https://en.wikipedia.org/wiki/University_of_Colorado_Boulder"
response = requests.get(url)

print(response.status_code)   # 200 means success
print(len(response.text))     # characters of raw HTML
```

Raw HTML isn't data yet. An API hands back JSON that drops straight into a
DataFrame:

```python
import pandas as pd

article = "University_of_Colorado_Boulder"
api = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
url = f"{api}/en.wikipedia/all-access/all-agents/{article}/daily/20240101/20240131"
headers = {"User-Agent": "WebDataScience/1.0 (you@colorado.edu)"}

data = requests.get(url, headers=headers).json()   # JSON -> dict
df = pd.DataFrame(data["items"])                   # list of dicts -> DataFrame
df.head()
```

If you get a DataFrame with dates and view counts, you're ready.

The `User-Agent` header identifies who is making the request — a politeness
norm we take seriously starting in Week 2.

---

## 2 · GitHub Desktop or the `gh` CLI

This course works entirely through GitHub — cloning the textbook, making a
change, opening a pull request — without ever typing a raw `git` command.
Pick whichever fits how you work; either is fine for every assignment this
semester.

### Option A: GitHub Desktop (recommended if this is new to you)

Download [GitHub Desktop](https://desktop.github.com) and sign in with your
GitHub account. That's the whole install — it bundles everything it needs, no
separate download.

Desktop gives you a button for everything you'll do this semester: **Clone** a
repository, create a **branch**, **commit** changes with a message, **push**,
and **Create Pull Request** — each one a click, not a command.

### Option B: the `gh` CLI (if you're comfortable in a terminal)

Install [`gh`](https://cli.github.com), then authenticate once:

```bash
gh auth login    # follow the prompts; browser sign-in is easiest
```

`gh` needs Git itself present underneath (macOS/Linux usually already have it;
Windows: install [Git for Windows](https://git-scm.com/downloads) alongside
`gh`) — but you'll interact through `gh`'s commands, not raw `git` ones:

```bash
gh repo clone cuinfoscience/Web-Data-Science-Book
gh pr create                        # from a branch with your changes committed
gh pr view --web                    # open your PR in the browser
```

One-time only: tell Git who you are, so your commits are attributed to you —
this is the one identity detail `gh` doesn't set for you:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@colorado.edu"
```

---

## 3 · A free GitHub account

Create one at [github.com](https://github.com). **Sign up with your
`colorado.edu` email** to unlock free student features via the
[GitHub Student Developer Pack](https://education.github.com/pack).

Then go star the course textbook so it's easy to find:
[cuinfoscience/Web-Data-Science-Book](https://github.com/cuinfoscience/Web-Data-Science-Book)

---

## Troubleshooting

**`conda: command not found`** — the installer didn't add conda to your `PATH`.
On macOS/Linux, restart your terminal; if that fails, run the installer's
`conda init` step. On Windows, use the "Anaconda Prompt" application.

**`ModuleNotFoundError` for a library you just installed** — your notebook is
probably running a different kernel than the environment you installed into.
Check with `import sys; print(sys.executable)` inside the notebook and confirm
it points at your `webdata` environment.

**`ConnectionError` or a 403 on the request above** — check that you're online,
and that you included the `User-Agent` header. Some services reject requests
that don't identify themselves.

**Can't access a laptop or install software?** Contact me **immediately** so we
can arrange an accommodation. Do not wait until an assignment is due.
