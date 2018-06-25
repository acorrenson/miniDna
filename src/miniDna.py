
"""MiniDna : an introduction to Bioinformatics
  
  MiniDna is a python project to discover the incredible
  world of Bioinformatics. This module provides some
  basic functions to compare, translate and study DNA sequences

  Author: Arthur Correnson
  Email: arthur.correnson@gmail.com

  (c) 2018

  MiniDna may be freely distributed under the MIT license.
  (license file can be found in the parent directory)
"""

import math, random

# all nucleotides
NUCLEOTIDES = 'ATGC'

# codon to amino acid table
AMINOCODE =  {
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

AMINO = {
  'A': 'Alanine', 
  'F': 'Phenyl-alanine', 
  'L': 'Leucine',
  'P': 'Proline',
  'H': 'Histidine',
  'Q': 'Glutamine',
  'R': 'Arginine',
  'I': 'Isoleucine',
  'T': 'Threonine', 
  'N': 'Asparagine',
  'K': 'Lysine',
  'S': 'Serine',
  'V': 'Valine',
  'D': 'Aspartic acid',
  'E': 'Glutamic acid',
  'G': 'Glycine'
}

def isAdn(seq: str) -> bool: 
  """Test if a string is a DNA sequence.

    Keyword arguments:
    seq -- the string to test
  """
  nuc = ['A', 'T', 'G', 'C']
  for n in seq:
    if n not in nuc:
      print("Invalid DNA sequence")
      return False
  return True


def percentIdentical(seqA: str, seqB: str) -> float:
  """ Return the percentage of identity between two DNA sequences.
    
    Keyword arguments:
    seqA -- the first sequence
    seqB -- the second sequence
  """
  if len(seqA) != len(seqB):
    raise ValueError("sequences have unequal length")
  dist = sum(ch1 != ch2 for ch1, ch2 in zip(seqA, seqB))
  return math.ceil(100 * (1 - dist/len(seqA)))



def identityProbability(gs: int, mr: float = 1e-08) -> float:
  """Return the probabilty for a sequence 
    to not change over n generations of evolution.
    
    Keyword arguments:
    gs -- number of generations
    mr -- mutation rate (default is 1e-08)
  """
  return math.pow(1-mr, gs)


def freqList(seqList: list, prob: bool = True) -> dict:
  """Return the frequency of each nucleotide in each
    position.

    Keyword argument:
    seqList -- DNA sequences list
    prob -- False: return a dictionnary of probability (between 0 and 1)
            True: return a dictionnary of freqency (int)
            Default is True
  """
  n = len(seqList[0])
  nl = len(seqList)
  freqs = {
    'A': [0]*n,
    'T': [0]*n,
    'G': [0]*n,
    'C': [0]*n
  }
  for seq in seqList:
    for i, nuc in enumerate(seq):
        freqs[nuc][i] += 1
  if prob:
    for key in freqs:
      for i in range(len(freqs[key])):
        freqs[key][i] = freqs[key][i]/nl
  return freqs

def freqAt(freqDict: dict, nuc: str, n: int) -> float:
  """Read a frequency dictionnary returned 
    by the function freqList.

    Keyword arguments:
    freqDic -- frequence dictionnary
    nuc -- nucleotide A,T,G or C
    n -- position
  """
  return freqDict[nuc][n]

def translate(seq: str) -> str:
  """find the protein coded in a DNA sequence
    
    Keyword arguments:
    seq -- DNA sequence to translate
  """
  start = 0
  protein = ''
  while start+2 < len(seq):
    codon = seq[start:start+3]
    protein += AMINOCODE[codon]
    start += 3
  return protein


def dotPlot(seqA: str, seqB: str) -> list:
  """Compare two DNA sequences using DotPlot method.

    Keyword arguments:
    seqA -- first sequence
    seqB -- second sequence
  """
  la = len(seqA)
  lb = len(seqB)
  M = [[' ' for n in range(la)] for m in range(lb)]
  for i in range(lb):
    for j in range(la):
      if seqB[i] == seqA[j]:
        M[i][j] = 'x'
  return M


def filterDotPlot(seqA: str, seqB: str, k: int) -> list:
  """Compare two DNA sequences using DotPlot method 
    keep only K long equals sequences

    Keyword arguments:
    seqA -- first sequence
    seqB -- second sequence
    k -- minimum length of equal portions
  """
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


def compare(seqA: str, seqB: str) -> None:
  """Compare two sequences.
    Display the result in the console

    Keyword arguments:
    seqA -- first sequence (DNA or Protein)
    seqB -- first sequence (DNA or Protein)
  """
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


def display(a: str, b: str, m: list) -> None:
  """Display dotplot matrix properly
    
    Keyword arguments:
    a -- first sequence compared
    b -- second sequence compared
    m -- dotplot matrix
  """
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

print('\n')

print("frequency :\n")
print(freqList([a, b])['A'])