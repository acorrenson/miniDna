from tabulate import tabulate

# test if a string is a DNA sequence
def isAdn(seq: str) -> bool: 

  nuc = ['A', 'T', 'G', 'C']

  for n in seq:
    if n not in nuc:
      print("Invalid DNA sequence")
      return False
  return True
# -------------------------

# simple comparison of 2 DNA sequences using DotPlot
def dotPlot(seqA: str, seqB: str, k: int):

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
def filterDotPlot(seqA: str, seqB: str, k:int):

  if isAdn(seqA) and isAdn(seqB):
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

def compare(seqA: str, seqB: str):

  if isAdn(seqA) and isAdn(seqB):
    la = len(seqA)
    lb = len(seqB)
    
    sim = ''

    for n in range(la):
      if seqA[n] == seqB[n]:
        sim += '|'
      else:
        sim += '-'

    print('======|=' + '=' * len(seqA))
    print(' seqA | ' + seqA)
    print(' ---- | ' + sim)
    print(' seqB | ' + seqB)
    print('======|=' + '=' * len(seqA))


# display dotplot properly
def display(a, b, m):

  header = '  '

  for c in a:
    header += (c + ' ')

  print(header)
  print('==' * len(a) + '===')

  for i in range(len(m)):
    s = b[i] + ' '
    for j in range(len(m[0])):
      s += (m[i][j] + ' ')

    print(s)
# -------------------------


# test
a = 'ATGCCGCTAACGTA'
b = 'ATGCCACTACCGTA'

m = filterDotPlot(a, b, 3)

# display(a, b, m)
print('DotPlot\n')
display(a, b, m)

print('\n')

print('Simple comparison\n')
compare(a, b)
# -------------------------

