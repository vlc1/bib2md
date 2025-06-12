#!/bin/bash

BASENAME=${1%.bib}

echo $BASENAME

echo  "
\select@language{english}
\citation{*}
\bibstyle{mybst}
\bibdata{$BASENAME}" > $BASENAME.aux

bibtex $BASENAME
pandoc -f latex  $BASENAME.bbl -o $BASENAME.md

rm $BASENAME.aux
rm $BASENAME.blg
rm $BASENAME.bbl
