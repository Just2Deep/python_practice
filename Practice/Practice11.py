# count occurences of an element in a list

# Method 1 iteration
import pandas as pd
import operator as op
from collections import Counter
from itertools import count


def countX(list, x):
    count = 0

    for i in list:
        if i == x:
            count += 1

    return count


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 2, 1, 2, 3, 34, 245, 2, 4, 7, 3, 4]
print(countX(list1, 4))

# Method 2 using count function

print(list1.count(4))


# Method 3 Using counter function

l = Counter(list1)

x = 4
print(f'{x} has occured {l[x]} times')


# Method 4 using countof functions

y = 2
print(f'{y} has occured {op.countOf(list1, y)} times')


# Method 5 using dict comprehensions

check = 'e'
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b']
count_val = {item: list2.count(item) for item in list2}
print(count_val[check])

# Method 6 using pandas


# declaring the list
pl = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

count = pd.Series(list2).value_counts()
print('Element Count')
print(count)
