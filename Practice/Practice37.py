# Python Program to print all Possible Combinations from the three Digits

# naive method

from itertools import permutations
test_list = [1, 2, 3]
n = len(test_list)
list1 = []

for i in range(n):
    for j in range(n):
        for k in range(n):
            if (i != j and j != k and k != i):
                print(test_list[i], test_list[j], test_list[k], sep=', ')

# permutations from itertools


perm = permutations(test_list, n)
print([i for i in perm])
