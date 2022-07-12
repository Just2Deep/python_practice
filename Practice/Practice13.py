# Summation of number digits in a list

# Brute force 2 for loops

from functools import reduce
from matplotlib.pyplot import pink


list1 = [12, 31, 45, 42]
list_new = []

for i in list1:
    sum1 = 0
    for digit in str(i):
        sum1 += int(digit)

    list_new.append(sum1)

print(list_new)


# Using sum and list comprehensions

new_list = list(map(lambda x: sum(int(sub)for sub in str(x)), list1))
print(f' the new list is {new_list}')


print('----------------')
# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + list comprehension
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))

# printing result
print("List Integer Summation : " + str(res))


# Using SUM and Reduce
res2 = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in list1]
print(res2)


list2 = [12, 67, 98, 34, 25, 96]

res3 = list(map(lambda i: sum(int(sub) for sub in str(i)), list2))
print('checking new output ', res3)
