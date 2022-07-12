# Cloning/Copying a list

# Method 1 using slicing

import copy
li1 = [4, 8, 2, 10, 15, 18]

li2 = li1[:]
print(li1)
print(li2)

# Method 2 using extend method
li3 = []
li3.extend(li1)
print(li3)

# Method 3 using assignment operator

li4 = li1
print(li4)

# Method 4 using copy

li5 = copy.copy(li1)
print(li5)


# Method 5 using list comprehensions

li6 = [i for i in li1]
print(li6)


# Method 6 using append

li7 = []
for i in li1:
    li7.append(i)

print(li7)

# Method 7 using built in copy

li8 = li1.copy()
print(li8)

# Method 8 using deepcopy

li9 = copy.deepcopy(li1)
print(li9)
