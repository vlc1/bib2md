SHELL=/bin/bash

default: einstein.md

%.md: %.bib mybst.bst
	@bash bib2md.bash $<

clean:
	@rm -f einstein.md
