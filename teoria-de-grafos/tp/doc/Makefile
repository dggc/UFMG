SHELL=/bin/bash
TEX=tp.tex \
		descricao.tex formulacao.tex casos-especiais.tex complexidade.tex propriedades.tex relacao.tex \
		implementacao.tex descricao-algoritmo.tex estruturas.tex decisoes.tex \
	 	resultados.tex experimentos-qualidade.tex experimentos-eficiencia.tex \
		conclusao.tex

tp.pdf: $(TEX) tp.bib 
	pdflatex tp.tex
	bibtex tp
	pdflatex tp.tex
	pdflatex tp.tex

clean:
	rm -f *.aux *.log *.out *.pdf *.bbl *.blg *.bak *.toc

check: $(TEX)
		for tex in $(TEX); do aspell -c $$tex -l pt-br; done

see: tp.pdf
	evince tp.pdf &
