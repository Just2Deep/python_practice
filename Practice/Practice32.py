#  List product excluding duplicates

from functools import reduce

# using lambda , set and reduce

test_list = [1, 3, 5, 6, 3, 5, 6, 1]


def ProductUnique(li):
    unique = []
    output = reduce(lambda x, y: x*y, set(li), 1)

    return output


print(ProductUnique(test_list))


# using list comprehensions

sum_val = 1
new_list = [i for i in list(set(test_list))]

for i in new_list:
    sum_val *= i

print(sum_val)
