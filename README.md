# miniDna

An introduction to bioinformatics !

# Purposes

MiniDna is a python module designed to be an introduction to bioinformatics.
It provides some basic functions to compare, sort and study DNA sequences.

! MiniDna is'nt a professionnal tool, it is just an educationnal project !

# References

All functions provided in the module are listed here :

```Python

# check if a given string is a DNA sequence
isDna(seq: str) # -> bool

# compare two sequences using DotPlot method
# return a matrice of dots showing similarities
DotPlot(seqA: str, seqB: str) # -> list

# compare two squences using DotPlot method
# return a matrice of dots showing only similar portions
# of the sequences longer or equal to K
FilterDotPlot(seqA: str, seqB: str, k: int) # -> list

display(seqA: str, seqB: str, m: list)

```

# Documentation

### isDna(seq)

Check if the given string is a Dna sequences (containing only nucleotides A T G C)

Parameters : 
+ seq : `str` String to check

Output :
+ bool

### DotPlot(seqA, seqB)

Compare two sequences using DotPlot method.
return a matrice of dots showing similarities.

Parameters :
+ seqA : `str` first Dna sequence to compare
+ seqB : `str` second Dna sequence to compare

Output :
+ list : a matrice of dots showing similarities betwen both sequences

### FilterDotPlot(seqA, seqB, k)

Compare two squences using DotPlot method.
return a matrice of dots showing only similar portions
of the sequences longer or equal to K.

Parameters :
+ seqA : `str` first Dna sequence to compare
+ seqB : `str` second Dna sequence to compare
+ k : `int` size of the compared portions




