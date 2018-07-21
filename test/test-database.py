# -*- coding: utf-8 -*-

import sys

sys.path.append('../src')

from miniDna.database import *

data = getData('hsa:3219')
aaseq = seqOfData(data, "AASEQ")
ntseq = seqOfData(data, "NTSEQ")

print(len(aaseq))
print(aaseq)

print(len(ntseq))
print(ntseq)


print(getNtSeq('hsa:3219'))
