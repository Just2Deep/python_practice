# Finding smallest number in a list

# Brute force

list1 = [1, 2, 3, 5, 7, 9, -1, 2]

small = list1[0]

for i in list1:
    if i < small:
        small = i

print(small)

# Sorting and printing first element

l2 = sorted(list1)
print(l2[0])

# Using min method

print(min(list1))


# User inputs for elements

list2 = []

num = int(input('Enter the number of elements in list: '))
for i in range(num):
    ele = input('enter the element: ')
    list2.append(ele)

print(f'The smallest number in the list is {min(list2)}')
