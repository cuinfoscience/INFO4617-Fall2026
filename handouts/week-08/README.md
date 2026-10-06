# Set up Selenium for chapter 8

*Do this before Wednesday's lab — INFO 4617 Web Data Science, week 8 — about 20 minutes*

Chapter 8 uses **Selenium**, a Python package that opens a real Chrome
window and controls it from your code: it visits pages, clicks, types, and
reads what the page shows. Anaconda comes with neither Selenium nor
**Selenium Manager**, the program Selenium uses to set up Chrome. So
chapter 8's browser code stops at its first line until you install them.

This page takes you from Anaconda as you installed it to chapter 8's own
notebook opening Chrome. The notebook does the work: its first Selenium
cell installs both packages, and the cells after it check each step before
Chrome opens. You won't need a terminal unless something goes wrong. Keep
the notebook afterwards, because Wednesday's lab uses it.

You don't need the course's `webdata` environment from week 1. If you made
it, these steps work there too, and the install cell says that everything
is already installed.

## What you need

- **Anaconda**, installed. Nothing else from week 1.
- **A fast internet connection.** The first run downloads up to about
  250 MB. Use home Wi-Fi, not the campus network five minutes before class.
- **Google Chrome, if you have it.** If you don't, that's fine: Selenium
  Manager downloads its own copy, Chrome for Testing.

## Words you'll see

| Word | What it means |
|---|---|
| **package** | Code that someone else wrote, which you add to Python. Selenium is one. Anaconda came with many others, such as `pandas` and `requests`. |
| **conda** | Anaconda's installer. It downloads packages and adds them to your Python. In a notebook, `%conda` at the start of a line runs it for the notebook's own Python. |
| **conda-forge** | A community collection of packages that conda can install from. This course's packages come from it. |
| **cell** | A box in a notebook that holds code or text. You run a code cell with **Shift+Enter**. |
| **kernel** | The Python behind an open notebook. When you run a cell, the kernel runs it. **Restarting the kernel** starts that Python fresh. Your notebook keeps its code, but the kernel forgets what earlier cells did. |
| **driver** | A small program, made for one version of Chrome, through which Python controls Chrome. You never download it yourself. |
| **Selenium Manager** | The program that finds your Chrome and downloads the matching driver, and Chrome for Testing too if you have no Chrome. conda installs it as a package of its own, `selenium-manager`. It keeps its downloads in a folder named `.cache/selenium` in your home folder. |
| **terminal** | A window where you type commands. On Windows, use **Anaconda Prompt**. On a Mac, use **Terminal**. You need one only if the notebook can't install Selenium. |

## 1 · Download chapter 8's notebook

1. Open chapter 8's notebook on GitHub:
   <https://github.com/cuinfoscience/Web-Data-Science-Book/blob/main/notebooks/ch-08-dynamic-pages.ipynb>.
   GitHub shows it as a page you can read, but you can't run it there.
2. Above the notebook, on the right, there's a **Raw** button and two small
   icons after it. Click the second icon, **Download raw file** (an arrow
   pointing down). Your browser saves `ch-08-dynamic-pages.ipynb` in your
   **Downloads** folder.
3. Check the file's name. It must end in `.ipynb`. If your computer named it
   `ch-08-dynamic-pages.ipynb.txt` or `.json`, rename it so that it ends in
   `.ipynb`. On Windows, File Explorer may hide the end of the name. To show
   it, choose **View → Show → File name extensions**.

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

1. In Jupyter's list, click **Downloads**, then **ch-08-dynamic-pages.ipynb**.
   The notebook opens in a new tab.
2. If you don't see the file, click **Upload** at the top right of the list,
   choose the file, and click the blue **Upload** button that appears next
   to its name. Then click the file to open it.
3. If Jupyter asks you to choose a kernel, choose **Python 3 (ipykernel)**.

Jupyter may say **Not Trusted** at the top right. That's normal for a
notebook you downloaded, and it doesn't stop the cells from running. If
Navigator opened **JupyterLab** instead, it works the same way: the list of
files is in the panel on the left.

## 4 · Install Selenium and Selenium Manager

1. Scroll down to the heading **Setting Up Selenium**, and below it,
   **Installing Selenium and Selenium Manager**. You can run the cells above
   it first, if you like. They fetch pages with `requests`, which Anaconda
   has.
2. Click the cell that says

   ```
   %conda install -y -c conda-forge selenium selenium-manager
   ```

   and press **Shift+Enter**. While it runs, `[*]` shows at its left. It
   takes a minute or two.
3. Read the end of what it printed. It worked if you see
   `The following NEW packages will be INSTALLED:`, with `selenium` and
   `selenium-manager` under it, and then `Executing transaction: done`. If
   you had both already, it says `All requested packages already installed`.
   conda may also print notices about other things, some starting with
   `WARNING`. They don't matter here.
4. Restart the kernel: choose **Kernel → Restart Kernel…**, then click
   **Restart**.

## 5 · Check each step, then open Chrome

Keep going down the notebook, under **Before the First Browser**. Click each
code cell and press **Shift+Enter**, then check what it printed:

| Cell | What it prints when it works |
|---|---|
| **Step 1** (settings) | `selenium 4.` and a version, then `Selenium Manager:` and a path ending in `selenium-manager`. If the path part says `inside the selenium package`, your Selenium came from `pip`, which also works. |
| **Step 2** (run Selenium Manager) | Selenium Manager's report, on a pink background. The pink doesn't mean an error: Jupyter colors everything sent to Python's error stream. The first time, it downloads the driver, and Chrome for Testing if you have no Chrome, so it can take several minutes. Its last lines start with `Driver path:` and `Browser path:`. No line should start with `WARNING`. |
| **Step 3** (check before you start the browser) | Two paths that end in `(found)`, then `Driver chosen by Selenium Manager: True`. |
| **Starting the Browser** (`driver = webdriver.Chrome()`) | A Chrome window opens. Leave it alone. The cell prints the browser's version and the driver's. They should match up to the first dot. |

When Chrome has opened, you're ready for Wednesday. Close Chrome from the
notebook, not with the mouse. Click **+** in the toolbar to add a cell, type
`driver.quit()`, and press **Shift+Enter**.

Each time you open the notebook again, such as on Wednesday, run step 1
before the browser cell. Step 1's settings last only until the kernel
restarts. You won't need the install cell again: Selenium stays installed,
and Selenium Manager keeps its downloads.

## Installing from a terminal instead

Use this if the install cell can't install the packages, or if you'd rather
use a terminal.

1. Open a terminal:
   - **Windows:** open **Anaconda Prompt** from the Start menu.
   - **Mac:** open **Terminal**, from Applications → Utilities.
2. The line where you type starts with `(base)`. That means your commands go
   to Anaconda's Python. On a Mac, if you don't see `(base)`, type
   `conda activate` and press Enter.
3. Type `conda install -c conda-forge selenium selenium-manager` and press
   Enter. When conda asks `Proceed ([y]/n)?`, type `y` and press Enter. Wait
   for `Executing transaction: done`.
4. Check it: `conda list selenium` lists both packages, and
   `selenium-manager --version` prints Selenium Manager's version.
5. Go back to the notebook, restart the kernel, and go on with step 5 above.

## When something goes wrong

| What you see | What to do |
|---|---|
| The notebook opens as a page of text, or its name ends in `.txt` or `.json` | Download it again with **Download raw file**, or rename it so that it ends in `.ipynb`. |
| Jupyter's list doesn't show the file | Use **Upload**, as in step 3. |
| `ModuleNotFoundError: No module named 'selenium'` | Run the install cell (step 4), restart the kernel, then go on. |
| The install cell says `EnvironmentNotWritableError`, or that you don't have write permissions | Anaconda was installed for every user of the computer. On Windows, right-click **Anaconda Prompt** in the Start menu, choose **Run as administrator**, and install from there, as above. |
| A cell has shown `[*]` for more than 10 minutes | The download is slow. Wait, or stop the cell with **Kernel → Interrupt Kernel** (■ in the toolbar), move to a faster network, and run the cell again. |
| Step 2 stops with `error sending request`, or mentions a connection | Your network blocked the download. Try another network, such as home Wi-Fi. |
| Step 3 shows `(MISSING)`, or ends with `False` | Run step 1, then steps 2 and 3 again. Step 1 tells Selenium Manager to skip old drivers on your computer. |
| The browser cell fails with `Unable to obtain driver for chrome` | Selenium couldn't find Selenium Manager. Run step 1, then the browser cell again. |
| The browser cell fails with `This version of ChromeDriver only supports Chrome version` | An old driver was used. Run steps 1 to 3, then the browser cell again. |
| The browser cell fails with `Chrome instance exited`, on Ubuntu 24.04 or later | Install Google Chrome from <https://www.google.com/chrome/>, then run steps 2 and 3 and the browser cell again. |
| Something still fails after a download broke halfway | Delete the folder `.cache` → `selenium` in your home folder, then run steps 1 to 3 again. On a Mac, Finder hides folders whose names start with a dot. Press **Cmd+Shift+.** to show them. |
| Anything else | Bring everything the failing cell printed, from its first line to its last, to Wednesday's lab. Or e-mail it before then to [brian.keegan@colorado.edu](mailto:brian.keegan@colorado.edu). |

Chapter 8's "When Selenium Manager Fails" lists more causes and fixes.
