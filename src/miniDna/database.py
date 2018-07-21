"""Database submodule of miniDna

  This submodule is a little wrapper for the KEGG api.
  It allows users to browse KEGG databases and download
  data from it.
  
  Kegg website :
  https://www.kegg.jp/
"""

# -*- coding: utf-8 -*-

import urllib.request
import math

def getData(name: str, method: str = 'get') -> str:
  """Get a sequence in the KEGG database.

    **Keyword arguments:**  
    name -- entry to get  
    method -- method of the KEGG API to use (default is 'get')  
    - 'get'  -> get data  
    - 'info' -> information on an entry  
    - 'list' -> list of all entries in a database  
    
    [KEGG API documentation](https://www.kegg.jp/kegg/rest/keggapi.html)

    Example:  
    humanGenome = getData('hsa', 'list')
  """

  r = urllib.request.urlopen('http://rest.kegg.jp/{0}/{1}'.format(method, name))
  txt = r.read().decode('utf-8')
  return txt


def getNtSeq(name: str):
  """Get a nucleotide sequence from the KEGG database

    **Keyword arguments:**  
    name -- entry to get
  """
  r = urllib.request.urlopen('http://rest.kegg.jp/get/{0}/ntseq'.format(name))
  data = r.read().decode('utf-8')
  lines = _stringToList(data)
  seq = "".join(s for s in lines[1:len(lines)])
  return seq


def getAaSeq(name: str):
  """Get a nucleotide sequence from the KEGG database

    **Keyword arguments:**  
    name -- entry to get
  """

  r = urllib.request.urlopen('http://rest.kegg.jp/get/{0}/aaseq'.format(name))
  data = r.read().decode('utf-8')
  lines = _stringToList(data)
  seq = "".join(s for s in lines[1:len(lines)])
  return seq


def seqOfData(data: str, seqType: str = 'NTSEQ'):
  """Extract a nucleotide sequence or an amino
    acid sequence from data fetched with
    getData function.
    
    **Keyword arguments:**  
    data -- a string returned by getData function  
    seqType -- type of sequence  
    - "NTSEQ" -> nucleotide sequence  
    - "AASEQ" -> amino acid sequence

  """

  def readSize(line):
    """read the size of the sequence"""
    s = ''
    for c in line:
      if c in '0123456789':
        s += c
    return int(s)

  txt = _stringToList(data)
  startIndex = 0

  for i, lines in enumerate(txt):
    if lines[0:5] == seqType:
      startIndex = i

  size = readSize(txt[startIndex])
  rows = math.ceil(size/60)
  start = startIndex + 1
  end = start + rows

  seq = "".join(s for s in txt[start:end])

  return seq.replace(" ", "")


def _stringToList(str: str) -> list:
  """Convert a string containing endLine char into
    a list.
  """

  l = []
  s = ''
  for c in str:
    if c == '\n':
      l.append(s)
      s = ''
    else:
      s += c
  l.append(s)
  return l