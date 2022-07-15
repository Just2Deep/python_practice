# Python | Reverse All Strings in String List

# initializing list
test_list = ["geeks", "for", "geeks", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# Method 1: List comprehensions

res = [i[::-1] for i in test_list]

print("The modified list is : " + str(res))

# Method 2: map and lambda

result = list(map(lambda x: x[::-1], test_list))
print("The modified list is : " + str(result))
