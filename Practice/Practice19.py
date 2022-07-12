# Finding odd numbers in a list

# Using for loop

list1 = [10, 21, 4, 45, 66, 93]

for i in list1:
    if i % 2 != 0:
        print(i, end=" ")

print()
# using while loop

i = 0

while(i < len(list1)):
    if list1[i] % 2 != 0:
        print(list1[i], end=' ')

    i += 1
print()

# using list comprehensions

print([x for x in list1 if x % 2 != 0])

# using lambda expressions

res = list(filter(lambda x: (x % 2 != 0), list1))
print(res)
