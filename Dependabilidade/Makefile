FILE=dependabilidade

.PHONY: all see clean cleanall

all:
	pdflatex ${FILE}
	pdflatex ${FILE}
	bibtex ${FILE}
	pdflatex ${FILE}

clean: 
	rm -f *.aux *.toc *.log *.dvi

cleanall: clean
	rm -f ${FILE}.pdf

see:
	evince ${FILE}.pdf &
