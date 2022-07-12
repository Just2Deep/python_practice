# Remove all the occurrences of an element from a list in Python

# Method 1 : Using list comprehension


test_list = [1, 3, 4, 6, 5, 1]
item = 1


def removeOc(test_list, item):

    return [i for i in test_list if i != item]


print(removeOc(test_list, item))


# Method 2 : Using filter()

new_list = filter(lambda x: x != item, test_list)
print(list(new_list))


# Method 3 : Using remove method

for i in test_list:
    if i == item:
        test_list.remove(i)

print(test_list)
