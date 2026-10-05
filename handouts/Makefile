# Build the handouts from their Quarto and LaTeX sources (see README.md).
#
#   make            every handout's PDF, and each Quarto handout's notebook
#   make check      rerun each handout's code against the live pages
#   make figures    rebuild the annotated screenshots (img/*_annotated.tex)
#
# Needs Quarto, pdfLaTeX (TeX Live), and Python 3; `make check` also needs
# requests, beautifulsoup4, pandas, nbformat, nbclient, and ipykernel.

QUARTO ?= quarto
PYTHON ?= python3

QMD    := $(wildcard week-*/*.qmd)
TEX    := $(wildcard week-*/*.tex)
PDF    := $(QMD:.qmd=.pdf) $(TEX:.tex=.pdf)
IPYNB  := $(QMD:.qmd=.ipynb)
FIGTEX := $(wildcard week-*/img/*_annotated.tex)
COMMON := common/handout.cls common/handoutmarkers.sty \
          common/handout-template.tex common/handout.lua

# the images a handout in folder $(1) can show: each .png and .pdf in its img/
# but an _annotated.png with an _annotated.pdf beside it, a raster copy for the
# notebook. So a figure synced there again, or redrawn from its .tex, rebuilds
# the handout, and the records (shots.json, IMAGES.md) rebuild nothing.
images_in = $(filter-out $(addsuffix .png,$(basename $(wildcard $(1)img/*_annotated.pdf))),\
              $(wildcard $(1)img/*.png $(1)img/*.pdf))

.PHONY: all pdf notebooks figures check
all: pdf notebooks
pdf: $(PDF)
notebooks: $(IPYNB)
figures: $(FIGTEX:.tex=.pdf) $(FIGTEX:.tex=.png)

# from here, $$ in a rule's prerequisites waits for the rule's stem, $$*
.SECONDEXPANSION:

%.pdf: %.qmd $(COMMON) $$(call images_in,$$(dir $$*))
	cd $(dir $<) && $(QUARTO) render $(notdir $<) --to pdf

# a handout written in LaTeX with handout.cls: a PDF, and no notebook
%.pdf: %.tex common/handout.cls common/handoutmarkers.sty $$(call images_in,$$(dir $$*))
	cd $(dir $<) && latexmk -pdf -interaction=nonstopmode -halt-on-error $(notdir $<) \
	  && latexmk -c $(notdir $<)

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
