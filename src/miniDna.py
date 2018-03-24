from tabulate import tabulate

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

  M = [[' ' for n in range(la)] for m in range(lb)]

  for i in range(lb):
    for j in range(la):
      if seqB[i] == seqA[j]:
        M[i][j] = 'x'

  return M
# -------------------------

# comparison of DNA sequences using DotPlot 
# keep only K long equals sequences  
def FilterDotPlot(seqA: str, seqB: str, k:int):

  la = len(seqA)
  lb = len(seqB)

  M = [[' ' for n in range(la)] for m in range(lb)]

  for i in range(lb + 1 - k):
    for j in range(la + 1 - k):
      a = seqA[j:j+k]
      b = seqB[i:i+k]

      if a == b:
        for d in range(k):
          M[i+d][j+d] = 'x'

  return M
# -------------------------

# display dotplot properly
def display(a, b, m):
  for i in range(len(m)): m[i] = [b[i]] + m[i]
  print( tabulate(m, a, tablefmt = "simple") ) 
# -------------------------

a = 'ATGCC'
b = 'ATGCC'

m = FilterDotPlot(a, b, 2)

display(a, b, m)

