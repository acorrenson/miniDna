# miniDna

An introduction to bioinformatics !

# Purposes

MiniDna is a python module designed to be an introduction to bioinformatics.
It provides some basic functions to compare, sort and study DNA sequences.

! MiniDna is'nt a professionnal tool, it is just an educationnal project !

# Thanks

# Dependencies

Python : `v3.~` 


# References

All functions provided in the module are listed here :

```Python

isDna(seq: str) # -> bool

dotPlot(seqA: str, seqB: str) # -> list

filterDotPlot(seqA: str, seqB: str, k: int) # -> list

compare(seqA: str, seqB: str)

display(seqA: str, seqB: str, m: list)

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
Return a matrice showing similarities between sequence A and B. 
A similarity is marked with a X character in the matrice. 
A difference is marked with a space character in the matrice. 

Parameters :
+ seqA : `str` first Dna sequence to compare
+ seqB : `str` second Dna sequence to compare

Output :
+ `list` / `str` : matrice

### filterDotPlot(seqA, seqB, k)

Compare two squences using DotPlot method.
Return a matrice of dots showing only similar portions
of the sequences longer or equal to K.

Parameters :
+ seqA : `str` first Dna sequence to compare
+ seqB : `str` second Dna sequence to compare
+ k : `int` size of the compared portions

### compare(seqA, seqB)

Verry simple comparison of 2 DNA sequences. 
Equal nucleotides are marked with a vertical bar. 
Different nucleotides are marked with a horinzontal bar. 

Display the result in the console.

Parameters :
+ seqA : `str` first Dna sequence to compare
+ seqB : `str` second Dna sequence to compare

Output :
+ `null`

### display(seqA, seqB, m)

Display a matrice generated with *dotPlot* or *filterDotPlot* functions in the console.

+ seqA : `str` sequence (row)
+ seqB : `str` sequence (column)
+ m : `list` / `str` matrice

Output :
+ `null`





