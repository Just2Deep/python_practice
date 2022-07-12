# Program to print duplicates from a list of integers

from collections import Counter
from itertools import count
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]


# brute force
check = []
dup = []
for i in list1:
    if i not in check:
        check.append(i)
    elif i not in dup:
        dup.append(i)

print(dup)

# using Counter

count_list = Counter(list1)

print([x for x in count_list if count_list[x] > 1])

# using count

new = []

for i in list1:
    if list1.count(i) > 1 and i not in new:
        new.append(i)

print(new)

# using list comprehensions

dup_count = list(set([x for x in list1 if list1.count(x) > 1]))
print(dup_count)


# using dict and  list

new_dict = {}
new_list = []

for i in list1:
    if not i in new_dict:
        new_dict[i] = 1
    else:
        new_dict[i] += 1

for key, values in new_dict.items():
    if values > 1:
        new_list.append(key)

print(new_list)
