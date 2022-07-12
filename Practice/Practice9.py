# Reversing a list in python

# Method 1 using insert

list = [1, 2, 3, 4, 5, 6, 7]

l = []

for i in list:
    l.insert(0, i)

print(l)

# Method 2 using reversed func

l2 = reversed(list)
l2 = [i for i in l2]
print(l2)


# Method 3 modify original list by reverse

list.reverse()
print(list)

list.reverse()

# Method 4 using slicing

l3 = list[::-1]
print(l3)
