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

# make_stubs.py draws placeholders for missing images and updates only the
# marked table in img/IMAGES.md; its output stays visible so a skipped or
# failed step is not silent.
$(WEEKS):
	@echo "==> $@"
	@cd $@ && if [ -f img/stubs.tsv ]; then python3 ../common/make_stubs.py . \
	  || echo "  make_stubs.py failed; building without new placeholders"; fi
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
