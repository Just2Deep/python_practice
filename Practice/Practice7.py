# Check if element exists in python

# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

print("Checking if 4 exists in list ( using loop ) : ")

for i in test_list:
    if i == 4:
        print('Element exists')

#using in operator

if 4 in test_list:
    print('Element Exists')
else:
    print('No')

# Using count func

count = test_list.count(4)

if count > 0:
    print('Exists')
else:
    print('Nope')
