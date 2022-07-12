# Python program to find all the Combinations in the list with the given condition

# initializing list
test_list = ["geekforgeeks", [5, 4, 3, 4],
             "is", ["best", "good", "better", "average"]]

# printing original list
print("The original list is : " + str(test_list))

k = 4
res = []

for idx in range(k):
    temp = []
    for i in test_list:
        if not isinstance(i, list):
            temp.append(i)
        else:
            temp.append(i[idx])

    res.append(temp)

print("The modified list is : " + str(res))
