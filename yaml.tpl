---
references:
$for(references)$
  - id: $references.id$
    type: $references.type$
    title: $references.title$
$if(references.author)$
    author:
$for(references.author)$
      - family: $references.author.family$
        given: $references.author.given$
$endfor$
$endif$
$if(references.issued)$
    issued:
      year: $references.issued.year$
      month: $references.issued.month$
      day: $references.issued.day$
$endif$
$if(references.container-title)$
    container-title: $references.container-title$
$endif$
$if(references.volume)$
    volume: "$references.volume$"
$endif$
$if(references.issue)$
    issue: "$references.issue$"
$endif$
$if(references.page)$
    page: "$references.page$"
$endif$
$if(references.DOI)$
    DOI: "$references.DOI$"
$endif$
$if(references.URL)$
    URL: "$references.URL$"
$endif$

$endfor$
---
