# How to count unique values inside a list

from collections import Counter
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

li = []

for i in input_list:
    if i not in li:
        li.append(i)

print(len(li))


# Method 2 using Counter


new_list = Counter(input_list)
print(len(new_list.keys()))


# Method 3 using set

set_method = set(input_list)
print(len(set_method))
