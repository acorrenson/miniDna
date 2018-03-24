from  tabulate import *

# test if a string is a DNA sequence
def isAdn(seq: str) -> bool: 

  nuc = ['A', 'T', 'G', 'C']

  for n in brin:
    if n not in nuc:
      return False
  return True
# -------------------------

# simple comparison of 2 DNA sequences using DotPlot
def DotPlot(seqA: str, seqB: str, k: int):

  la = len(seqA)
  lb = len(seqB)

  M = [[0 for n in range(la)] for m in range(lb)]

  for i in range(lb):
    for j in range(la):
      if seqB[i] == seqA[j]:
        M[i][j] = 1

  return M
# -------------------------

# comparison of DNA sequences using DotPlot 
# keep only K long equals sequences  
def FilterDotPlot(seqA: str, seqB: str, k:int):

  la = len(seqA)
  lb = len(seqB)

  M = [[0 for n in range(la)] for m in range(lb)]

  for i in range(lb + 1 - k):
    for j in range(la + 1 - k):
      a = seqA[j:j+k]
      b = seqB[i:i+k]

      if a == b:
        for d in range(k):
          M[i+d][j+d] = 1

  return M
# -------------------------


a = 'ATGCC'
b = 'ATGCC'

m = FilterDotPlot(a, b, 2)

print( tabulate(m) )

