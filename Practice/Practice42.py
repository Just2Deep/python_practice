# Python – Replace index elements with elements in Other List

# Method 1 List comprehensions

# Initializing lists
test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

new = []
final_list = [new.append(test_list1[i]) for i in test_list2]

# for i in test_list2:
#    final_list.append(test_list1[i])

print("The final list is : " + str(new))

# Method lambda and map method

f_list = list(map(lambda x: test_list1[x], test_list2))
print("Output from map", f_list)
