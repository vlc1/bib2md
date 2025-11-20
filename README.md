# How to use

Run `make einstein.md` to turn the following `.bib` file
```
@article{Einstein1905a,
	title = {Über einen die {Erzeugung} und {Verwandlung} des {Lichtes} betreffenden heuristischen {Gesichtspunkt}},
	volume = {322},
	number = {6},
	journal = {Annalen der Physik},
	author = {Einstein, A.},
	year = {1905},
}

@article{Einstein1905b,
	title = {Ist die {Trägheit} eines {Körpers} von seinem {Energieinhalt} abhängig?},
	volume = {323},
	number = {13},
	journal = {Annalen der Physik},
	author = {Einstein, A.},
	year = {1905},
}

```
into
```
1.  A. Einstein. **Ist die Trägheit eines Körpers von seinem
    Energieinhalt abhängig?** *Annalen der Physik*, 323(13), 1905

2.  A. Einstein. **Über einen die Erzeugung und Verwandlung des Lichtes
    betreffenden heuristischen Gesichtspunkt**. *Annalen der Physik*,
    322(6), 1905

```

# Usage

- Bibliography entries in CSL to YAML format
```bash
pandoc -s -f csljson -t markdown --template=yaml.tpl refs.json -o refs.md
```

# Credits

Based off a [blog post](https://members.loria.fr/EJeandel/posts/bibtex/) from Emmanuel Jeandel.
