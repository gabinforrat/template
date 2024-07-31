PAPER = article

all:
	pdflatex -shell-escape $(PAPER).tex
clean :
	rm $(PAPER).log $(PAPER).out $(PAPER).aux $(PAPER).toc
	rm -r _minted-$(PAPER)/
