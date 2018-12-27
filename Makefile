thesis.pdf: $(wildcard *.tex) $(wildcard chapters/natlog/*.tex)  $(wildcard chapters/naturalli/*.tex) $(wildcard chapters/openie/*.tex) $(wildcard chapters/qa/*.tex)  Makefile macros.tex std-macros.tex ref.bib
	@pdflatex thesis
	@bibtex thesis
	@pdflatex thesis
	@pdflatex thesis

clean:
	rm -f *.aux *.log *.bbl *.blg present.pdf *.bak *.ps *.dvi *.lot *.bcf thesis.pdf

dist: thesis.pdf
	@pdflatex --file-line-errors thesis

default: thesis.pdf
