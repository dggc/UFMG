SHELL=/bin/bash
TEX=apresentacao.tex

apresentaca.pdf: $(TEX) ../doc/tp.bib 
	pdflatex apresentacao
	bibtex apresentacao
	pdflatex apresentacao
	pdflatex apresentacao

clean:
	rm -f *.aux *.log *.out *.pdf *.bbl *.blg *.bak *.toc *.nav *.snm

check: $(TEX)
		for tex in $(TEX); do aspell -c $$tex -l pt-br; done

see: apresentacao.pdf
	evince apresentacao.pdf &
