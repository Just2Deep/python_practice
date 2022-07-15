# Python program to find the character position of Kth word from a list of strings

# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
# Output : 0
# Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 15
# Output : 1
# Explanation : 15th index occurs in “best” and point to “e” which is 1st element of word.

# initializing list
from itertools import count
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 20

# enumerate to get indices of all inner and outer list
res = [ele[0] for sub in enumerate(test_list) for ele in enumerate(sub[1])]

print("Index of character at Kth position word : " + str(res[K]))

# Method 2 : Using next() + zip() + count()

# Using next() + zip() + count()

# initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 20

# count() for getting count
# pairing using zip()
cnt = count()
res = next(j for sub in test_list for j, idx in zip(
    range(len(sub)), cnt) if idx == K)

# printing result
print("Index of character at Kth position word : " + str(res))
