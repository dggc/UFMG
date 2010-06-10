tp.pdf: tp.tex tp.bib 
	pdflatex tp.tex
	bibtex tp
	pdflatex tp.tex
	pdflatex tp.tex

clean:
	rm -f *.aux *.log *.out *.pdf *.bbl *.blg *.bak *.toc

check:
	aspell -c tp.tex -l pt-br

see: tp.pdf
	evince tp.pdf &
