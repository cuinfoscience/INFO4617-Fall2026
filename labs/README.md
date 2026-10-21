# Lab notebooks

From week 10, Wednesday and Friday are one live-coding lab: we write the code together, and Friday picks up where Wednesday stopped, before the revision block. What you submit is the chapter's Recommended Exercises, in its companion notebook; the lab prepares you for them. Each week has one notebook, in a folder named for the week, as in `slides/` and `handouts/`. Its text explains each step, and its code cells hold only a comment that says what to write. The lab itself isn't submitted.

This term began the labs in week 10. The labs for weeks 1–9 are written for the next time the course runs, and you're welcome to work through them.

| Week | Your copy | Solutions |
| --- | --- | --- |
| 1 · Introduction to web data science | [`week-01/lab-01.ipynb`](week-01/lab-01.ipynb) | [`week-01/lab-01-key.ipynb`](week-01/lab-01-key.ipynb) |
| 2 · Ethics, law, and responsible collection | [`week-02/lab-02.ipynb`](week-02/lab-02.ipynb) | [`week-02/lab-02-key.ipynb`](week-02/lab-02-key.ipynb) |
| 3 · The post-API age | [`week-03/lab-03.ipynb`](week-03/lab-03.ipynb) | [`week-03/lab-03-key.ipynb`](week-03/lab-03-key.ipynb) |
| 4 · Data formats: XML and JSON | [`week-04/lab-04.ipynb`](week-04/lab-04.ipynb) | [`week-04/lab-04-key.ipynb`](week-04/lab-04-key.ipynb) |
| 5 · Web architecture and protocols | [`week-05/lab-05.ipynb`](week-05/lab-05.ipynb) | [`week-05/lab-05-key.ipynb`](week-05/lab-05-key.ipynb) |
| 6 · Parsing static web pages | [`week-06/lab-06.ipynb`](week-06/lab-06.ipynb) | [`week-06/lab-06-key.ipynb`](week-06/lab-06-key.ipynb) |
| 7 · Archived web pages and the Wayback Machine | [`week-07/lab-07.ipynb`](week-07/lab-07.ipynb) | [`week-07/lab-07-key.ipynb`](week-07/lab-07-key.ipynb) |
| 8 · Dynamic web pages with Selenium | [`week-08/lab-08.ipynb`](week-08/lab-08.ipynb) | [`week-08/lab-08-key.ipynb`](week-08/lab-08-key.ipynb) |
| 9 · Extracting data from PDFs | [`week-09/lab-09.ipynb`](week-09/lab-09.ipynb) | [`week-09/lab-09-key.ipynb`](week-09/lab-09-key.ipynb) |
| 10 · Wikipedia's APIs | [`week-10/lab-10.ipynb`](week-10/lab-10.ipynb) | [`week-10/lab-10-key.ipynb`](week-10/lab-10-key.ipynb) |

## Get the notebook

1. Click the week's notebook in the table above, or open the week's folder (`week-10`) and click `lab-10.ipynb`.
2. Click **Download raw file** in the file toolbar (the down-arrow icon). If your browser opens the raw JSON instead, right-click the button and choose **Save Link As…**
3. Save it in the folder you use for the course's notebooks, and open it in JupyterLab in the `webdata` environment.

## Use it in class

- Read each step's text, then write the code in the cell under it as we write it together. The comment says what the cell should do.
- After each step, a **💬 Discuss** box holds a few questions we'll talk over before moving on. Click it to open it; there's nothing to write down.
- Put your own email address in the User-Agent in Step 0: every request you send carries it.
- If a cell fails, read the error before running it again. A **429** means Wikimedia's rate limit: wait the number of seconds it gives, and run the cell again.
- Fell behind? Copy the cell from the key and keep going.

## Solutions

`week-NN/lab-NN-key.ipynb` is the same notebook with every cell filled in and run. Its first cell gives the date it was run, and its outputs show what yours should print. Open it on GitHub to read it, or download it the same way. Live data changes, so a number that differs a little from the key may be a newer count, not a mistake.

## For maintainers

[`AUTHORING.md`](AUTHORING.md) says how to write a lab. In short: each lab lives in `week-NN/`; the key is the source, and `tools/make_student_copy.py` makes the students' copy from it; `tools/run_key.py` runs the key against the live sites, puts the placeholder email back, and refuses to write it if an output holds an API key.
