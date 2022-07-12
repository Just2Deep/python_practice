# Remove multiple elements from a list in Python

list1 = [3, 15, 10, 12]
rem = [3, 15]
print(list1)

li = []
for i in list1:
    if i not in rem:
        li.append(i)


print(li)

# using slicing to remove a part of the list

list2 = [11, 5, 17, 18, 23, 50]

del list2[1:5]

print(list2)
