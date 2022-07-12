# Finding the second largest element in a list

list1 = [10, 20, 4, 3, 56, 64, 245, 6453, 2335, 3254]

# sorting

list2 = list(list1)
list2.sort()
print(list2[-2])

# Optimal method

mx = max(list1[0], list1[1])
second_max = min(list1[0], list1[1])

for i in range(2, len(list1)):
    if list1[i] > mx:
        second_max = mx
        mx = list1[i]
    elif list1[i] > second_max and mx != list1[i]:
        second_max = list1[i]
    elif mx == second_max and second_max != list1[i]:
        second_max = list1[i]

print(second_max)

l3 = list(list1)
l3.remove(max(l3))
print(max(l3))

# Traversing twice


def FindSecondLargest(Arr):
    largest = Arr[0]
    Second = Arr[0]

    for i in Arr:
        if i > largest:
            largest = i

    for i in Arr:
        if i > Second and i != largest:
            Second = i

    return Second


print(f'Second Largest Element is', FindSecondLargest(list1))


print(max([x for x in list1 if x < max(list1)]))
