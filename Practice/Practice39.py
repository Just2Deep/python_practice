# Python program to get all unique combinations of two Lists

from itertools import permutations
from itertools import product

List_1 = ["a", "b"]
List_2 = [1, 2]

# Method 1 : Using permutation() of itertools package and zip() function.

unique = []
res = permutations(List_1, len(List_2))
#print([i for i in res])

for i in res:
    zipped = zip(i, List_2)
    unique.append([i for i in zipped])

print(unique)

# Method 2 : Using product() of itertools package and zip() function.

unique_combinations = list(list(zip(List_1, element))
                           for element in product(List_2, repeat=len(List_1)))
print(unique_combinations)
