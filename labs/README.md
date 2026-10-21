# Lab notebooks

From week 10, Wednesday's lab is live coding: we write the code together, and the lab carries on into Friday when it runs over. Each week has one notebook, in a folder named for the week, as in `slides/` and `handouts/`. Its text explains each step, and its code cells hold only a comment that says what to write. Nothing is submitted.

| Week | Your copy | Solutions |
| --- | --- | --- |
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

Each lab lives in `week-NN/`, as `lab-NN.ipynb` and `lab-NN-key.ipynb`. The lab notebooks are written directly as notebooks, not built from a `.qmd`, so nothing in `handouts/`'s `make` or workflow touches them. Requests in them are live, with no saved copies: the User-Agent and pacing are part of the lesson. Before committing a key, replace the email address you ran it with by `your-email@colorado.edu`, and check that no API key appears in its outputs. A lab is written in its week's sprint, alongside the chapter and slides, so it follows the chapter as it is that week. Week 10 is a pilot; if it works, each later week gets one too.
