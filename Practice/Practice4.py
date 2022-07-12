# methods find the length of a list

# Initializing list
from unittest import TestLoader


test_list = [1, 4, 5, 7, 8]

# Method 1 looping
count = 0
for i in test_list:
    count += 1

print(count)


# Method 2 built in function len

print(len(test_list))
