# Remove empty List from List

from itertools import product
import random
test_list = [5, 6, [], 3, [], [], 9]

# using list comprehensions

new_list = [x for x in test_list if x]
print(new_list)

# using filter
res = list(filter(None, test_list))
print(res)


# Convert List to List of dictionaries

test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list = ['name', 'id']
output = []

n = len(test_list)

for i in range(0, n, 2):
    output.append({key_list[0]: test_list[i], key_list[1]: test_list[i+1]})

print(output)

# using dict and list comprehensions

print([{key_list[0]:test_list[i], key_list[1]:test_list[i+1]}
      for i in range(0, len(test_list), 2)])


# Convert Lists of List to Dictionary
# initializing list
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
print("The original list is : " + str(test_list))

res1 = {}

for sub in test_list:
    res1[tuple(sub[:2])] = sub[2:]
print(res1)


print({tuple(sub[:2]): tuple(sub[2:]) for sub in test_list})


#  Uncommon elements in Lists of List

# initializing lists
test_list1 = [[1, 2], [3, 4], [5, 6]]
test_list2 = [[3, 4], [5, 7], [1, 2]]

# printing both lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

res3 = []
for i in test_list1:
    if i not in test_list2:
        res3.append(i)

for i in test_list2:
    if i not in test_list1:
        res3.append(i)

print('Uncommon', res3)

# using set, list and ^

res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
res_list = list(map(list, res_set))
print(res_list)


# Python program to select Random value form list of lists

# Using random.choice() [if row number given]

# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Row number
r_no = 2

# choice() for random number, from_iterables for flattening
res = random.choice(test_list[r_no])

# printing result
print("Random number from Matrix Row : " + str(res))


# Reverse Row sort in Lists of List

# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
print("The original list is : " + str(test_list))

for i in test_list:
    i.sort(reverse=True)
print(test_list)


# list comprehension
sorted_list = [sorted(i, reverse=True) for i in test_list]
print(sorted_list)


#map and sorted

sorted_list2 = list(map(lambda x: sorted(x, reverse=True), test_list))
print(sorted_list2)


# Python – Pair elements with Rear element in Matrix Row

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

res_1 = []
for i in test_list:
    res_1.append([[ele, i[-1]] for ele in i[:-1]])

print(res_1)


# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# Pair elements with Rear element in Matrix Row
# using product() + loop
res = []
for idx in test_list:
    res.append(list(product(idx[:-1], [idx[-1]])))

# printing result
print("The list after pairing is : " + str(res))
