# Test if List contains all elements in given Range

# Initializing loop
test_list = [4, 5, 6, 7, 3, 9, 11]

# printing original list
print("The original list is : " + str(test_list))

# Initialization of range
i, j = 3, 10

res = True
for val in test_list:
    if val < i or val > j:
        res = False
        break

# printing result
print("Does list contain all elements in range : " + str(res))

# Method 2 : Using all()

res2 = all(ele >= i and ele < j for ele in test_list)
print("Does list contain all elements in range : " + str(res2))
