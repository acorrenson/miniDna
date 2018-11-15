# miniDna

An introduction to bioinformatics !

# Purposes

MiniDna is a python project I coded in order to discover the incredible world of bioinformatics.
It provides some basic functions to compare, sort and study DNA sequences.

# References

[*Alignements par pair*](http://pedagogix-tagc.univ-mrs.fr/courses/bioinfo_intro/pdf_files/03.02.alignements_par_paires_fr.pdf)
+ course written by : Jacques van Helden
+ University of Aix-Marseille, France

[*Bioinformatique 2eme édition*](https://www.dunod.com/sciences-techniques/bioinformatique-cours-et-applications)
+ book written by : Gilbert Deléage & Manolo Gouy
+ edition : Dunod

[*Computaional Biology*](https://brilliant.org/courses/computational-biology/) 

# Dependencies

Python : `v3.~`

Python modules :
+ urllib
+ math
+ random

# Examples

Here are two simple examples of what we can do with the miniDna module : 

```Python

# load data from KEGG database
# (Here we are looking for a human gene
# coding for histamine receptor)
data = getData("hsa:3269")

# extract the nucleotide sequence
seq = seqOfData(data, "NTSEQ")

# translate the nucleotide sequence into
# an amino acid sequence
aminoSeq = translate(seq)

# output : 
# MSLPNSSCLLEDKMCEG...
```

# Documentation

The documentation can be read here : [*miniDna documentation*](https://jdrprod.github.io/miniDna)
