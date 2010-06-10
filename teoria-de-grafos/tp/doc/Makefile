TEX=tp.tex descricao.tex implementacao.tex resultados.tex conclusao.tex

tp.pdf: $(TEX) tp.bib 
	pdflatex tp.tex
	bibtex tp
	pdflatex tp.tex
	pdflatex tp.tex

clean:
	rm -f *.aux *.log *.out *.pdf *.bbl *.blg *.bak *.toc

check:
	for t in $(TEX)
		do
		aspell -c $t -l pt-br
	done

see: tp.pdf
	evince tp.pdf &
