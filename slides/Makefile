# Build every weekly lecture deck.
#   make            build all decks (regenerates image stubs first)
#   make week-06    build a single week
#   make stubs      (re)generate placeholder images from each img/stubs.tsv
#   make clean      remove LaTeX build artifacts (keeps the deck PDF)
#
# The shared Gotham theme, preamble, and bibliography live in common/ and are
# put on TEXINPUTS/BIBINPUTS so each deck compiles from inside its own folder.

WEEKS := $(sort $(wildcard week-*))
TEXENV := TEXINPUTS=../common: BIBINPUTS=../common:
LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all stubs clean $(WEEKS)

all: $(WEEKS)

$(WEEKS):
	@echo "==> $@"
	@cd $@ && [ -f img/stubs.tsv ] && python3 ../common/make_stubs.py . >/dev/null 2>&1 || true
	@cd $@ && $(TEXENV) $(LATEXMK) $@.tex
	@cd $@ && $(TEXENV) $(LATEXMK) $@.tex >/dev/null 2>&1   # 2nd pass: resolve citations

stubs:
	@for w in $(WEEKS); do [ -f $$w/img/stubs.tsv ] && python3 common/make_stubs.py $$w || true; done

clean:
	@for w in $(WEEKS); do \
	  rm -f $$w/*.aux $$w/*.bbl $$w/*.blg $$w/*.bcf $$w/*.run.xml \
	        $$w/*.fdb_latexmk $$w/*.fls $$w/*.log $$w/*.nav $$w/*.out \
	        $$w/*.snm $$w/*.toc $$w/*.vrb; \
	done
	@echo "cleaned build artifacts (deck PDFs kept)"
