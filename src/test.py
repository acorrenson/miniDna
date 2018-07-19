
from miniDna import *

# # test
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

print('\n')

seqa = "AATCATGC"
seqb = "TTTGCATT"

seqb, seqa = simpleAlign(seqb, seqa)

compare(seqb, seqa)

print("\n")

a, b = globalAlign("MPRCLCQRINCYA", "PYRCKCRNICIA", 3, -1, -2)

print("\n")

# print(translate(ntOfData(getData('hsa:3269'))))

print("\n")

# print(aaOfData(getData('hsa:3269')))

print(seqOfData(getData('hsa:3269'), "AASEQ"))

print("\n")

print(stringToList(getData('hsa:3269')))

print("END")
