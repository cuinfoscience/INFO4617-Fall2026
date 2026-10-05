# Getting set up

*Do this before Monday, August 24 — INFO 4617 Web Data Science*

Three things must work on your laptop before the first notebook lab. Allow about
45 minutes. If you cannot complete a step, send me an e-mail before Monday at
[brian.keegan@colorado.edu](mailto:brian.keegan@colorado.edu). Do not come to
class with an environment that does not work.

| | What | Why |
|---|---|---|
| 1 | **Python, with Anaconda** | The language, a set of scientific libraries, and the `conda` package manager |
| 2 | **GitHub Desktop or the `gh` CLI** | Sends the changes on your laptop to a pull request. You do not need `git` commands |
| 3 | **A free GitHub account** | Holds the textbook and receives your revisions |

---

## 1 · Python with Anaconda

Install Anaconda from [anaconda.com](https://www.anaconda.com/download). Then
make a separate environment for this course. The first command is one long
line:

```bash
conda create -n webdata --override-channels -c conda-forge python=3.14 notebook requests beautifulsoup4 lxml pandas matplotlib seaborn gensim dnspython selenium playwright-python pypdf pdfplumber praw spotipy atproto mastodon.py openai anthropic
conda activate webdata
```

The first command makes the environment and installs everything in it at
once: Python, Jupyter (`notebook`), and every library the textbook's chapters
import, from `requests` in week 1 to `openai` in week 13. They come from
conda-forge, a community channel that builds packages for new versions of
Python quickly. gensim, which week 7 uses, has no Python 3.14 build that `pip`
can install. Expect it to take a few minutes. Run `conda activate webdata`
each time you open a new terminal.

Only two later steps are not in this command. Week 8 downloads browsers for
Playwright (`playwright install chromium`), and weeks 11 to 13 ask you for
API keys.

### Made `webdata` before October 2?

The first version of this page installed fewer libraries. Add the rest once,
from a terminal (on Windows, the Anaconda Prompt). This is one long line:

```bash
conda install -n webdata -c conda-forge gensim lxml dnspython selenium playwright-python pypdf pdfplumber praw spotipy atproto mastodon.py openai anthropic
```

Type `y` when conda asks to proceed. If your `webdata` was made with `pip`, as
the first version of this page did, conda then prints thousands of lines that
start with `ClobberError`: pip and conda both installed some of the same
files. conda reports them and carries on. Let it finish; its last lines
include `Executing transaction: done`.

Then restart Jupyter itself, not just the kernel. In the terminal where
Jupyter runs, press Ctrl+C twice. Run `conda activate webdata`, then start
`jupyter notebook` again. Activating `webdata` tells Selenium where conda put
its driver manager, and a running Jupyter keeps the settings it started with,
so a kernel restart can import Selenium but can't start Chrome.

Use one environment for each project. The environment records the version of
each library that your analysis used. This makes your results reproducible. It
also prevents this course from damaging the libraries of a different project.

Start your workspace:

```bash
jupyter notebook
```

Jupyter opens in your browser, at a list of the files in the folder you
started it from. A notebook holds code, notes, and results in one file.

![Jupyter's file list in the browser, in Jupyter Notebook 7.6, September 2026 (the textbook's figure 1.1). This folder holds chapter 1's companion notebook (1). **New** (2) opens a menu whose first item, **Python 3 (ipykernel)** (3), makes a new notebook: started from `webdata`, that kernel is the environment's Python.](img/jupyter-new-menu_annotated.png)

> **Note:** do all coursework in Python. Do not use spreadsheet or business
> intelligence software (Excel, Tableau, Power BI) for assignments.

### Check that it works

Make a new notebook. Run the code that follows. One call gets a web page:

```python
import requests

# Identify yourself: Wikipedia answers the library's default User-Agent with a 403
headers = {"User-Agent": "WebDataScience/1.0 (your-email@colorado.edu)"}

url = "https://en.wikipedia.org/wiki/University_of_Colorado_Boulder"
response = requests.get(url, headers=headers)

print(response.status_code)   # 200 means success
print(len(response.text))     # characters of raw HTML
```

Raw HTML is not yet data. An API returns JSON. You can put JSON directly into a
DataFrame:

```python
import pandas as pd

article = "University_of_Colorado_Boulder"
api = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article"
url = f"{api}/en.wikipedia/all-access/all-agents/{article}/daily/20240101/20240131"
headers = {"User-Agent": "WebDataScience/1.0 (your-email@colorado.edu)"}

data = requests.get(url, headers=headers).json()   # JSON -> dict
df = pd.DataFrame(data["items"])                   # list of dicts -> DataFrame
df.head()
```

The setup is correct if you get a DataFrame with dates and view counts.

The `User-Agent` header tells the server who sends the request. Put your own
e-mail address in it. Wikipedia refuses a request that does not identify its
sender. Week 2 explains why this is important.

---

## 2 · GitHub Desktop or the `gh` CLI

This course uses GitHub for all revisions. You will copy the textbook, change
it, and open a pull request. You do not need to type a `git` command. Select
one of the two tools. Each tool is sufficient for every assignment this
semester.

### Option A: GitHub Desktop (select this if GitHub is new to you)

Download [GitHub Desktop](https://desktop.github.com). Sign in with your GitHub
account. The installation is then complete. Desktop includes all the software
that it needs.

Desktop gives you a button for each task in this course. You can **Clone** a
repository, make a **branch**, **commit** your changes with a message, **push**
them, and select **Create Pull Request**.

### Option B: the `gh` CLI (select this if you know how to use a terminal)

Install [`gh`](https://cli.github.com). Then authenticate one time:

```bash
gh auth login    # obey the prompts. Browser sign-in is the easiest method
```

`gh` needs Git on your computer. macOS and Linux usually include Git. On
Windows, also install [Git for Windows](https://git-scm.com/downloads). You
will use the `gh` commands, not the `git` commands:

```bash
gh repo clone cuinfoscience/Web-Data-Science-Book
gh pr create                        # use this in a branch that has your commits
gh pr view --web                    # opens your pull request in the browser
```

Do this one time. Give Git your name and e-mail address. Git puts them on each
commit. `gh` cannot set them for you:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@colorado.edu"
```

---

## 3 · A free GitHub account

Make an account at [github.com](https://github.com). Use your `colorado.edu`
e-mail address. This gives you the free student features in the
[GitHub Student Developer Pack](https://education.github.com/pack).

Then star the course textbook. You can then find it quickly:
[cuinfoscience/Web-Data-Science-Book](https://github.com/cuinfoscience/Web-Data-Science-Book)

---

## Troubleshooting

**`conda: command not found`** — the installer did not add conda to your `PATH`.
On macOS and Linux, start your terminal again. If the error continues, run the
`conda init` step of the installer. On Windows, use the "Anaconda Prompt"
application.

**`jupyter: command not found`** (or "not recognized" on Windows) — Jupyter
is not installed in the active environment. Run `conda activate webdata`,
then `conda install -c conda-forge notebook`, and start `jupyter notebook`
again.

**`ModuleNotFoundError` for a library that you installed** — your notebook
probably uses a different kernel than the environment. In the notebook, run
`import sys; print(sys.executable)`. Make sure that the path shows your
`webdata` environment.

**`ConnectionError` or a 403 error** — make sure that you have a network
connection. Also make sure that you included the `User-Agent` header. Some
servers refuse requests that do not identify the sender.

**No laptop, or you cannot install the software?** Tell me immediately. We will
arrange an accommodation. Do not wait until an assignment is due.
