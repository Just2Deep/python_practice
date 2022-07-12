# Python program to find the Strongest Neighbour

test_list = [1, 2, 2, 3, 4, 5]
new = []

for i in range(1, len(test_list)):
    new.append(max(test_list[i-1], test_list[i]))

print(new)
