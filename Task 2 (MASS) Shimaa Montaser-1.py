# setup library:
from pyopenms import *
import pyopenms

# Creating VAKA Sequance :

seq = AASequence.fromString("VAKA")

# Geting Seq Mass Each:
Sum = 0

for S in seq:
    Sum += S.getMonoWeight()

print(Sum)

# Mass of the seq is:
print(seq.getMonoWeight())
