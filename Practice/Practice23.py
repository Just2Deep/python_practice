# Python program to print positive numbers in a list

list1 = [12, -7, 5, 64, -14]

# looping
li = []
for i in list1:
    if i >= 0:
        li.append(i)

print(li)

# while loop
j = 0
while (j < len(list1)):
    if list1[j] >= 0:
        print(list1[j], end=' ')
    j += 1
print()
# list comphrension

print([x for x in list1 if x >= 0])

# using lambda
print(list(filter(lambda x: (x >= 0), list1)))
