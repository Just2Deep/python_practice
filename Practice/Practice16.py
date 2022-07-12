# Finding the largest number in the list

list1 = [10, 20, 4, 3, 56, 64, 245, 6453, 2335]

# brute force

large = list1[0]
for i in list1:
    if i > large:
        large = i

print(large)

# MAX func

print(max(list1))

# Using sort

l2 = sorted(list1)
list1.sort()
print(list1[-1])
print(l2[-1])
