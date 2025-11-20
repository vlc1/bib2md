default: input.md refs.bib
	@pandoc input.md --citeproc -t markdown_strict -o output.md

markdown: input.md refs.bib
	@pandoc input.md --citeproc -t markdown_strict -o output.md

clean:
	@rm -rf output.md
