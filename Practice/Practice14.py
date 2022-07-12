# Multiply all the numbers in a list

# Brute force

from operator import *
import math
from functools import reduce
from http.client import ImproperConnectionState
import numpy
l1 = [1, 2, 3, 4]
output = 1
for i in l1:
    output *= i

print(output)

# Using numpy

print(numpy.prod(l1))


output2 = reduce(lambda x, y: x*y, l1)
print(output2)

# using math


print(math.prod(l1))

# using operator module (mul)

num = 1
for i in l1:
    num = mul(i, num)

print(num)
