# Build the handouts from their Quarto sources (see README.md).
#
#   make            every handout's PDF and companion notebook
#   make check      rerun each handout's code against the live pages
#   make figures    rebuild the annotated screenshots (img/*_annotated.tex)
#
# Needs Quarto, pdfLaTeX (TeX Live), and Python 3; `make check` also needs
# requests, beautifulsoup4, pandas, nbformat, nbclient, and ipykernel.

QUARTO ?= quarto
PYTHON ?= python3

QMD    := $(wildcard week-*/*.qmd)
PDF    := $(QMD:.qmd=.pdf)
IPYNB  := $(QMD:.qmd=.ipynb)
FIGTEX := $(wildcard week-*/img/*_annotated.tex)
COMMON := common/handout.cls common/handoutmarkers.sty \
          common/handout-template.tex common/handout.lua

.PHONY: all pdf notebooks figures check
all: pdf notebooks
pdf: $(PDF)
notebooks: $(IPYNB)
figures: $(FIGTEX:.tex=.pdf) $(FIGTEX:.tex=.png)

%.pdf: %.qmd $(COMMON)
	cd $(dir $<) && $(QUARTO) render $(notdir $<) --to pdf

%.ipynb: %.qmd common/make_notebook.py
	$(PYTHON) common/make_notebook.py $<

# an annotated screenshot: vector PDF for the handout, PNG for the notebook
%_annotated.pdf: %_annotated.tex common/handoutmarkers.sty
	cd $(dir $<) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(notdir $<) \
	  && latexmk -c $(notdir $<)
%_annotated.png: %_annotated.pdf
	pdftoppm -png -singlefile -r 250 $< $(basename $@)

check:
	@for f in $(QMD); do $(PYTHON) common/check_outputs.py $$f || exit 1; done
