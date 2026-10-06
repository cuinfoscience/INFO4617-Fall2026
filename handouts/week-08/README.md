# Set up Selenium for chapter 8

*Do this before Wednesday's lab — INFO 4617 Web Data Science, week 8 — about 20 minutes*

Chapter 8 uses **Selenium**, a Python package that opens a real Chrome
window and controls it from your code: it visits pages, clicks, types, and
reads what the page shows. Anaconda doesn't come with Selenium, so chapter
8's code stops at its first line until you install it. This page takes you
from Anaconda as you installed it to a notebook that opens Chrome, visits a
page, and closes Chrome again. You won't need a terminal unless something
goes wrong.

You don't need the course's `webdata` environment from week 1. If you made
it, these steps work there too.

## What you need

- **Anaconda**, installed. Nothing else from week 1.
- **A fast internet connection.** The first run downloads up to about
  220 MB. Use home Wi-Fi, not the campus network five minutes before class.
- **Google Chrome, if you have it.** If you don't, that's fine: Selenium
  downloads its own copy, Chrome for Testing.

## Words you'll see

| Word | What it means |
|---|---|
| **package** | Code that someone else wrote, which you add to Python. Selenium is one. Anaconda came with many others, such as `pandas` and `requests`. |
| **pip** | Python's installer. It downloads a package from the Python Package Index ([pypi.org](https://pypi.org)) and adds it to your Python. |
| **cell** | A box in a notebook that holds code or text. You run a code cell with **Shift+Enter**. |
| **kernel** | The Python behind an open notebook. When you run a cell, the kernel runs it. |
| **driver** | A small program, made for one version of Chrome, through which Python controls Chrome. You never download it yourself. |
| **Selenium Manager** | A program that comes with Selenium. The first time your code starts Chrome, it finds your Chrome and downloads the matching driver. If you have no Chrome, it downloads Chrome for Testing too. It keeps its downloads in a folder named `.cache/selenium` in your home folder. |
| **terminal** | A window where you type commands. On Windows, use **Anaconda Prompt**. On a Mac, use **Terminal**. You need one only if the notebook can't install Selenium. |

## 1 · Download the setup notebook

1. Open the notebook on GitHub:
   <https://github.com/cuinfoscience/INFO4617-Fall2026/blob/main/handouts/week-08/selenium-setup.ipynb>.
   GitHub shows it as a page you can read, but you can't run it there.
2. Above the notebook, on the right, there's a **Raw** button and two small
   icons after it. Click the second icon, **Download raw file** (an arrow
   pointing down). Your browser saves `selenium-setup.ipynb` in your
   **Downloads** folder.
3. Check the file's name. It must end in `.ipynb`. If your computer named it
   `selenium-setup.ipynb.txt` or `selenium-setup.json`, rename it to
   `selenium-setup.ipynb`. On Windows, File Explorer may hide the end of the
   name. To show it, choose **View → Show → File name extensions**.

Don't click **Raw** itself. It shows the notebook as a page of text, all
`{` and `"`, and saving that page can give the file the wrong name.

## 2 · Open Jupyter

- **Windows:** open the Start menu, type **Anaconda Navigator**, and open it.
- **Mac:** open **Anaconda-Navigator** from your Applications folder.

Navigator can take a minute to start. Find the **Jupyter Notebook** tile
(it may say just **Notebook**) and click **Launch**. A tab opens in your web
browser with a list of the folders in your home folder. That tab is
Jupyter. Keep Navigator open while you work.

On Windows, you can also open **Jupyter Notebook (anaconda3)** from the
Start menu. It opens a black window as well. Leave that window open: closing
it stops Jupyter.

## 3 · Open the notebook in Jupyter

1. In Jupyter's list, click **Downloads**, then **selenium-setup.ipynb**.
   The notebook opens in a new tab.
2. If you don't see the file, click **Upload** at the top right of the list,
   choose the file, and click the blue **Upload** button that appears next
   to its name. Then click the file to open it.
3. If Jupyter asks you to choose a kernel, choose **Python 3 (ipykernel)**.

Jupyter may say **Not Trusted** at the top right. That's normal for a
notebook you downloaded, and it doesn't stop the cells from running. If
Navigator opened **JupyterLab** instead, it works the same way: the list of
files is in the panel on the left.

## 4 · Run it, one cell at a time

1. Click the first gray cell that holds code, and press **Shift+Enter**.
   Jupyter runs that cell and moves to the next one.
2. While a cell runs, `[*]` shows at its left. When it finishes, a number
   takes the star's place. Some cells take minutes, because they download.
3. Read the last line each cell prints:
   - **OK**: go on to the next cell.
   - **FIX**: do what it says, then run that cell again.
4. Keep going to the end. Step 5 opens Chrome, visits a page, closes Chrome,
   and says **OK … You're ready for chapter 8.**

What the five steps do:

1. **Install Selenium**, with the line `%pip install selenium`. `%pip` runs
   pip for the Python behind the notebook, Anaconda's, so you don't need a
   terminal. The cell after it checks that the install worked.
2. **Make two settings for Selenium Manager.**
3. **Run Selenium Manager by itself.** The first time, it downloads the
   driver, and Chrome for Testing if you have no Chrome. Its report shows on
   a pink background. The pink is Jupyter's color for that kind of report,
   not an error.
4. **Check what Selenium Manager found.**
5. **Open Chrome, visit a page, and close it**, as chapter 8's code does.

You install Selenium once. It stays installed, and Selenium Manager keeps
its downloads, so you won't do this again.

## 5 · Open chapter 8's notebook

1. Download it the same way, with **Download raw file**, from
   <https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/notebooks/ch-08-dynamic-pages.ipynb>.
2. Open it from Jupyter's list, as in step 3.
3. Run its cells in order. Its Selenium cells start under "Before the First
   Browser", and "Starting the Browser" opens Chrome. To be sure before
   Wednesday, run it that far.

## Installing from a terminal instead

Use this if step 1 of the notebook can't install Selenium, or if you'd
rather use a terminal.

1. Open a terminal:
   - **Windows:** open **Anaconda Prompt** from the Start menu.
   - **Mac:** open **Terminal**, from Applications → Utilities.
2. The line where you type starts with `(base)`. That means your commands go
   to Anaconda's Python. On a Mac, if you don't see `(base)`, type
   `conda activate` and press Enter.
3. Type `pip install selenium` and press Enter. Wait until it prints
   `Successfully installed`, followed by a list that includes `selenium`.
4. Go back to the notebook. Choose **Kernel → Restart Kernel…**, then run its
   cells again from the top. Step 1 now says that Selenium is already
   installed.

## When something goes wrong

| What you see | What to do |
|---|---|
| The notebook opens as a page of text, or its name ends in `.txt` or `.json` | Download it again with **Download raw file**, or rename it so that it ends in `.ipynb`. |
| Jupyter's list doesn't show the file | Use **Upload**, as in step 3. |
| A cell has shown `[*]` for more than 10 minutes | The download is slow. Wait, or stop the cell with **Kernel → Interrupt Kernel** (■ in the toolbar), move to a faster network, and run the cell again. |
| Step 1 says `Access is denied` or `Permission denied` | Anaconda was installed for every user of the computer. Do what the check cell under it says: add a cell with `%pip install --user selenium` and run it. Or install from a terminal, as above. |
| Step 3 says `error sending request` | Your network blocked the download. Try another network, such as home Wi-Fi. |
| You clicked in the Chrome window or closed it, and step 5 failed | Run step 5 again, and leave the window alone. |
| Something still fails after a download broke halfway | Delete the folder `.cache` → `selenium` in your home folder, then run steps 2 to 5 again. On a Mac, Finder hides folders whose names start with a dot. Press **Cmd+Shift+.** to show them. |
| Anything else | Bring everything the failing cell printed, from its first line to its last, to Wednesday's lab. Or e-mail it before then to [brian.keegan@colorado.edu](mailto:brian.keegan@colorado.edu). |

Chapter 8's "When Selenium Manager Fails" lists more causes and fixes.
