# -*- coding: utf-8 -*-

import sys

sys.path.append('../')

from src.miniDna.sequence import *

string = 'AGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCC'
print(string)
print("Is it a dna sequence ?", isDna(string))

print('\n')

print('Compare two sequences with dotPlot method :')
a = 'AGCTCCTAAGCCACTGC'
b = 'AGCTCCTGAGCCACTGC'
print(a)
print(b)
print()
display(a, b, dotPlot(a, b))

print('\n')

print('Compare two sequences with filterDotPlot method :')
display(a, b, filterDotPlot(a, b, 3))

print('\n')

print('Simple comparison betwenn two sequences :')
compare(a, b)

