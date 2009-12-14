FILE=apresentacao
.PHONY: clean see all cleanall

all :
	pdflatex ${FILE}
	pdflatex ${FILE}
	bibtex ${FILE}
	pdflatex ${FILE}


see:
	evince ${FILE}.pdf &

clean:
	rm -f *.log *.aux *.bbl *.nav *.out *.snm *.toc *.blg

cleanall: clean
	rm -f ${FILE}.pdf
