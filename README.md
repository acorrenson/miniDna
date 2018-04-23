# miniDna

An introduction to bioinformatics !

# Purposes

MiniDna is a python module I coded in order to discover the incredible world of bioinformatics.
It provides some basic functions to compare, sort and study DNA sequences.

MiniDna is'nt a professionnal tool, it is just an educationnal project !

# Thanks

I would like to quote 2 main sources that I used to do this project : 

[*Alignements par pair*](http://pedagogix-tagc.univ-mrs.fr/courses/bioinfo_intro/pdf_files/03.02.alignements_par_paires_fr.pdf)
+ course written by : Jacques van Helden
+ University of Aix-Marseille, France

["Bioinformatique 2eme édition"](https://www.dunod.com/sciences-techniques/bioinformatique-cours-et-applications)
+ book written by : Gilbert Deléage & Manolo Gouy
+ edition : Dunod

# Dependencies

Python : `v3.~` 

# References

All functions provided in the module are listed here :

```Python

isDna(seq: str) 
# return -> bool

dotPlot(seqA: str, seqB: str) # -> list

filterDotPlot(seqA: str, seqB: str, k: int)
# return -> list

compare(seqA: str, seqB: str)
# return -> null

display(seqA: str, seqB: str, m: list)
# return -> null

# --- more soon (wip) --- #

```

# Documentation

### isDna(seq)

Check if the given string is a Dna sequence (containing only nucleotides A T G C)

Parameters : 
+ seq : `str` String to check

Output :
+ bool

### dotPlot(seqA, seqB)

Compare two sequences using DotPlot method.
Return a matrix showing similarities between sequence A and B. 
Similarities are marked with a X character in the matrix. 
Differences are marked with a space character in the matrix. 

Parameters :
+ seqA : `str` first Dna sequence to compare
+ seqB : `str` second Dna sequence to compare

Output :
+ `list` / `str` : matrice

### filterDotPlot(seqA, seqB, k)

Compare two squences using DotPlot method.
Return a matrix of dots showing only similar portions
of the sequences which are at least k nulceotides long.

Parameters :
+ seqA : `str` first Dna sequence
+ seqB : `str` second Dna sequence
+ k : `int` minimum length

### compare(seqA, seqB)

Verry simple comparison of 2 DNA sequences. 
Equal nucleotides are marked with a vertical bar. 
Different nucleotides are marked with a horinzontal bar. 

Display the result in the console.

Parameters :
+ seqA : `str` first Dna sequence
+ seqB : `str` second Dna sequence

Output :
+ `null`

### display(seqA, seqB, m)

Display a matrix generated with *dotPlot* or *filterDotPlot* functions in the console.

+ seqA : `str` sequence (row)
+ seqB : `str` sequence (column)
+ m : `list` / `str` matrice

Output :
+ `null`





