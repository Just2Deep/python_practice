# Different ways to clear a list in python

# . clear method
# Creating list
GEEK = [6, 0, 4, 1]
print('GEEK before clear:', GEEK)

GEEK.clear()
print(GEEK)

# by reinitialization method
# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]

list2 = []

print(list2)


# using list*=0

list1 *= 0
print(list1)

# using del keyword
# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]

del list1[:]

print(list1)
