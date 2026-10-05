# Images in `week-08/img`

The figures of week 8's handout *Set up Selenium* (`../selenium-setup.tex`;
`make` in `handouts/`). The handout prints each `*_annotated.pdf`, and
`no-manager.png` and `selenium_browser.png` as they are.

All but `selenium_browser.png` are screenshots of a real Jupyter Notebook
7.6.3, captured on 2026-10-05 by the textbook's `tools/shots` from the
recipes `week08-handout-*` in its `tools/shots/recipes/course.yml`. The
markers were drawn from those recipes when `sync` copied the figures here.
The Jupyter was set up the way a student's is after adding Selenium to an
older `webdata` while Jupyter was running: started without
`conda activate`, so its kernels have no `SE_MANAGER_PATH`, as an ordinary
user on a computer with no Chrome. The notebook's cells are chapter 8's
own (steps 1 to 3 of "Before the First Browser", and the cell under
"Starting the Browser"), followed by the handout's visit cell.

- `setup-cell` — step 1 after it ran: (1) the Selenium version, (2) the
  Selenium Manager path that the cell found in `webdata`'s `bin` folder.
- `manager-log` — step 2's first run, with Selenium Manager's cache
  emptied before the take: (1) no Chrome, (2) Chrome for Testing
  downloaded, (3) chromedriver downloaded, (4) the paths in the cache. A
  take from a filled cache fails its recipe, so a retake needs the capture
  user's `~/.cache/selenium` emptied first.
- `check-paths` — step 3: (1) both paths found, (2) the driver is Selenium
  Manager's choice.
- `first-chrome` — the browser cell and the visit cell: (1) the browser's
  and the driver's versions, (2) the page's title.
- `no-manager` — two strips of the traceback when the browser cell runs
  without step 1 in that Jupyter, joined one above the other.
- `selenium_browser.png` — the same file as the week 8 slides' (see
  `slides/week-08/img/IMAGES.md`): the one screenshot allowed to show
  Chrome for Testing's bar, because the bar is what it shows
  (`slides/common/AUTHORING.md`).

<!-- shots:begin: copies from the textbook's tools/shots, generated from shots.json; edits between these markers are replaced -->
Copied here by the textbook's `tools/shots/run sync`; `tools/shots/run synced` checks them.

| File | Copy of | Captured | Source | How |
|---|---|---|---|---|
| `check-paths.png` and `check-paths_annotated.png` and `check-paths_annotated.pdf` | `course/week08-handout-check-paths` (tools/shots/out/course/week08-handout-check-paths/20261005T210458Z.png, textbook `1504b92`) | 2026-10-05 | http://localhost:8888/notebooks/selenium-setup.ipynb | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
| `first-chrome.png` and `first-chrome_annotated.png` and `first-chrome_annotated.pdf` | `course/week08-handout-first-chrome` (tools/shots/out/course/week08-handout-first-chrome/20261005T210506Z.png, textbook `1504b92`) | 2026-10-05 | http://localhost:8888/notebooks/selenium-setup.ipynb | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
| `manager-log.png` and `manager-log_annotated.png` and `manager-log_annotated.pdf` | `course/week08-handout-manager-log` (tools/shots/out/course/week08-handout-manager-log/20261005T210250Z.png, textbook `1504b92`) | 2026-10-05 | http://localhost:8888/notebooks/selenium-setup.ipynb | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×900 at 2× |
| `no-manager.png` | `course/week08-handout-no-manager` (tools/shots/out/course/week08-handout-no-manager/20261005T210357Z.png, textbook `1504b92`) | 2026-10-05 | http://localhost:8888/notebooks/no-setup-cell.ipynb | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
| `selenium_browser.png` | `course/week08-selenium-browser` (tools/shots/out/course/week08-selenium-browser/20261005T210544Z.png, textbook `1504b92`) | 2026-10-05 | https://xkcd.com/ | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2×, webdriver.Chrome() under Selenium 4.49.0 (ChromeDriver 154.0.8037.92) |
| `setup-cell.png` and `setup-cell_annotated.png` and `setup-cell_annotated.pdf` | `course/week08-handout-setup-cell` (tools/shots/out/course/week08-handout-setup-cell/20261005T210321Z.png, textbook `1504b92`) | 2026-10-05 | http://localhost:8888/notebooks/selenium-setup.ipynb | tools/shots: Google Chrome for Testing 154.0.8037.92, 800×600 at 2× |
<!-- shots:end -->
