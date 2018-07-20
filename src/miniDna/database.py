# -*- coding: utf-8 -*-

import urllib.request
import math
from . sequence import *

def getData(name: str, method: str = 'get') -> str:
  """Get a sequence in the KEGG database.

    **Keyword arguments:**  
    name -- name of the sequence to get  
    method -- method of the KEGG API to use (default is 'get')  

    Example:  
    data = getData('hsa:3269') 
  """

  r = urllib.request.urlopen('http://rest.kegg.jp/{0}/{1}'.format(method, name))
  txt = r.read().decode('utf-8')
  return txt


def seqOfData(data: str, seqType: str = "NTSEQ"):
  """Extract a nucleotide sequence or an amino
    acid sequence from data fetched with
    getData function.
    
    **Keyword arguments:**  
    data -- a string returned by getData function
    seqType -- type of sequence  
      "NTSEQ" -> nucleotide sequence  
      "AASEQ" -> amino acid sequence

  """
  i = 0
  while i < len(data):
    s = data[i:i+6]
    if s ==  seqType + " ":
      endLine = i
      c = data[endLine]
      while c != '\n':
        endLine += 1
        c = data[endLine]
      size = _len(data, i)
      rows = math.ceil(size/60)
      l = size + rows * 13
      if seqType == "NTSEQ":
        return _ntClean(data[endLine:endLine+l])
      else:
        return _aaClean(data[endLine:endLine+l])
    i += 1


def _ntClean(txt: str) -> str:
  """Convert a string containing nucleotides
    into a clean DNA sequence

    **Keyword arguments:**  
    txt -- input string
  """

  txt = txt.upper()
  nt = ""
  for c in txt:
    if c in NUCLEOTIDES:
      nt += c
  return nt.upper()


def _len(data: str, i: int) -> int:
  """Read the length of a sequence
    in a string returned by getData function

    **Keyword arguments:**  
    data -- a string returned by getData function  
    i -- index of the first char of the sequence  
        the sequence is read from char "N" for "NTSEQ"  
        the sequence is read from char "A" for "AASEQ"
  """

  sizeStr = ''
  j = i + 12
  c = data[j]
  while c != '\n':
    sizeStr += c
    j += 1
    c = data[j]
  return int(sizeStr)


def _aaClean(txt: str) -> str:
  """Convert a string containing amino acid
    into a clean amino acid sequence

    Keyword arguments:  
    txt -- input string
  """

  txt = txt.upper()
  aa = ""
  for c in txt:
    if c in AMINO:
      aa += c
  return aa

def stringToList(str: str) -> list:
  l = []
  s = ''
  for c in str:
    print(c)
    if c == '\n':
      l.append(s)
      s = ''
    else:
      s += c
  l.append(s)
  return l