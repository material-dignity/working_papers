# ════════════════════════════════════════════════════════════════════════════════
# Makefile
# Systemic Dignity Infrastructure: Working Paper Build System
#
# Usage:
#   make all      — Build all five papers
#   make wp1      — Build WP1 only
#   make wp2      — Build WP2 only
#   make wp3      — Build WP3 only
#   make wp4      — Build WP4 only
#   make wp5      — Build WP5 only
#   make clean    — Remove all build artifacts
#   make verify   — Check that all citation keys resolve
# ════════════════════════════════════════════════════════════════════════════════

LATEX   = pdflatex -interaction=nonstopmode -halt-on-error
BIBTEX  = bibtex

# Paper source definitions (Revised versions using shared template)
WP1_DIR = wp1_stewardship_model
WP1_SRC = ssrn-5968756_Revised

WP2_DIR = wp2_surplus_capacity
WP2_SRC = ssrn-6211658_Revised

WP3_DIR = wp3_los_angeles_pipeline
WP3_SRC = ssrn-6579600_Revised

WP4_DIR = wp4_human_layer
WP4_SRC = ssrn-6881539_Revised

WP5_DIR = wp5_economic_dignity
WP5_SRC = wp5_economic_dignity_Revised

.PHONY: all wp1 wp2 wp3 wp4 wp5 clean verify

all: wp1 wp2 wp3 wp4 wp5
	@echo "══════════════════════════════════════════"
	@echo "  All five papers compiled successfully."
	@echo "══════════════════════════════════════════"

wp1:
	@echo "Building WP1: Distributed Stewardship Model..."
	cd $(WP1_DIR) && $(LATEX) $(WP1_SRC) && $(BIBTEX) $(WP1_SRC) && $(LATEX) $(WP1_SRC) && $(LATEX) $(WP1_SRC)

wp2:
	@echo "Building WP2: Surplus Capacity..."
	cd $(WP2_DIR) && $(LATEX) $(WP2_SRC) && $(BIBTEX) $(WP2_SRC) && $(LATEX) $(WP2_SRC) && $(LATEX) $(WP2_SRC)

wp3:
	@echo "Building WP3: Los Angeles Pipeline..."
	cd $(WP3_DIR) && $(LATEX) $(WP3_SRC) && $(BIBTEX) $(WP3_SRC) && $(LATEX) $(WP3_SRC) && $(LATEX) $(WP3_SRC)

wp4:
	@echo "Building WP4: Human Layer..."
	cd $(WP4_DIR) && $(LATEX) $(WP4_SRC) && $(BIBTEX) $(WP4_SRC) && $(LATEX) $(WP4_SRC) && $(LATEX) $(WP4_SRC)

wp5:
	@echo "Building WP5: Economic Dignity..."
	cd $(WP5_DIR) && $(LATEX) $(WP5_SRC) && $(BIBTEX) $(WP5_SRC) && $(LATEX) $(WP5_SRC) && $(LATEX) $(WP5_SRC)

clean:
	@echo "Cleaning build artifacts..."
	find . -name "*.aux" -o -name "*.log" -o -name "*.bbl" \
	       -o -name "*.blg" -o -name "*.out" -o -name "*.toc" \
	       -o -name "*.lof" -o -name "*.lot" -o -name "*.fls" \
	       -o -name "*.fdb_latexmk" -o -name "*.synctex.gz" | xargs rm -f
	@echo "Clean complete."

verify:
	@echo "Verifying citation key resolution..."
	@for dir in $(WP1_DIR) $(WP2_DIR) $(WP3_DIR) $(WP4_DIR) $(WP5_DIR); do \
		echo "  Checking $$dir..."; \
		if ls $$dir/*.blg 1>/dev/null 2>&1; then \
			grep -c "Warning" $$dir/*.blg 2>/dev/null || echo "    No warnings."; \
		else \
			echo "    No .blg file found. Run 'make' first."; \
		fi; \
	done
