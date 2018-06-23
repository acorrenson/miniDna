# author: Arthur Correnson
# email: jdrprod@gmail.com

# (c) 2018

# miniDna may be freely distributed under the MIT license.
# (license file can be found in the parent directory)

import math, random

# all nucleotides
NUCLEOTIDES = 'ATGC'

# codon to amino acid table
AMINO =  {
  'ATG': 'M', 'GCG': 'A', 'TCA': 'S',
  'GAA': 'E', 'GGG': 'G', 'GGT': 'G',
  'AAA': 'K', 'GAG': 'E', 'AAT': 'N',
  'CTA': 'L', 'CAT': 'H', 'TCG': 'S',
  'TAG': 'STOP', 'GTG': 'V', 'TAT': 'Y',
  'CCT': 'P', 'ACT': 'T', 'TCC': 's',
  'CAG': 'Q', 'CCA': 'P', 'TAA': 'STOP',
  'AGA': 'R', 'ACG': 'T', 'CAA': 'Q',
  'TGT': 'C', 'GCT': 'A', 'TTC': 'F',
  'AGT': 'S', 'ATA': 'I', 'TTA': 'L',
  'CCG': 'P', 'ATC': 'I', 'TTT': 'F',
  'CGT': 'R', 'TGA': 'STOP', 'GTA': 'V',
  'TCT': 'S', 'CAC': 'H', 'GTT': 'V',
  'GAT': 'D', 'CGA': 'R', 'GGA': 'G',
  'GTC': 'V', 'GGC': 'G', 'TGC': 'C',
  'CTG': 'L', 'CTC': 'L', 'CGC': 'R',
  'CGG': 'R', 'AAC': 'N', 'GCC': 'A',
  'ATT': 'I', 'AGG': 'R', 'GAC': 'D',
  'ACC': 'T', 'AGC': 'S', 'TAC': 'Y',
  'ACA': 'T', 'AAG': 'K', 'GCA': 'A',
  'TTG': 'L', 'CCC': 'P', 'CTT': 'L', 
  'TGG': 'W'
} 

# test if a string is a DNA sequence
def isAdn(seq: str) -> bool: 

  nuc = ['A', 'T', 'G', 'C']

  for n in seq:
    if n not in nuc:
      print("Invalid DNA sequence")
      return False
  return True

# percentage of identity
def percentIdentical(seqA: str, seqB: str) -> float:
  if len(seqA) != len(seqB):
    raise ValueError("sequences have unequal length")

  dist = sum(ch1 != ch2 for ch1, ch2 in zip(seqA, seqB))
  
  return math.ceil(100 * (1 - dist/len(seqA)))

# probability of identity after n generations
def identityProbability(gs, mr = 1e-08):
  return math.pow(1-mr, gs)

def translate(seq):

  start = 0
  protein = ''

  while start+2 < len(seq):
    codon = seq[start:start+3]
    protein += AMINO[codon]
    start += 3

  return protein

# simple comparison of 2 DNA sequences using DotPlot
def dotPlot(seqA, seqB):

  la = len(seqA)
  lb = len(seqB)

  M = [[' ' for n in range(la)] for m in range(lb)]

  for i in range(lb):
    for j in range(la):
      if seqB[i] == seqA[j]:
        M[i][j] = 'x'

  return M

# comparison of DNA sequences using DotPlot 
# keep only K long equals sequences  
def filterDotPlot(seqA, seqB, k):

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

def compare(seqA, seqB):

  la = len(seqA)
  lb = len(seqB)
  
  sim = ''
  match = 0
  diff = 0

  for n in range(la):
    if seqA[n] == seqB[n]:
      sim += '|'
      match += 1
    else:
      sim += '-'
      diff += 1

  print('======|=' + '=' * len(seqA))
  print(' seqA | ' + seqA)
  print(' ---- | ' + sim)
  print(' seqB | ' + seqB)
  print('======|=' + '=' * len(seqA))
  print('======|> ' + str(diff) + ' differences')
  print('======|> ' + str(match) + ' matches')
  print('======|> ' + str(percentIdentical(seqA, seqB)) + '% identity')


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

# test
a = 'AGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCC'
b = 'AGCTCCTGAGCCACTGCCTGCTGGTGACCTTGGCTAGCCACCACCCTGCCGATTTCACCC'

m = filterDotPlot(a, b, 5)

print('DotPlot\n')
display(a, b, m)

print('\n')

print("percentIdentical :")
print(percentIdentical(a, b), "%")

print('\n')

print('DNA comparison :\n')
compare('TCTGCTTTAACTTAT', 'AGTGCGCTGACCTAC')

print('\n')

print("PROTEIN comparison :\n")
compare(translate('TCTGCTTTAACTTAT'), translate('AGTGCGCTGACCTAC'))