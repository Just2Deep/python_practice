# Printing even numbers in a list

# Brute force/traversing

list1 = [10, 21, 4, 45, 66, 93]
new = []

for i in list1:
    if i % 2 == 0:
        print(i, end=' ')

print()
# using while loop

num = 0
while (num < len(list1)):
    if list1[num] % 2 == 0:
        print(list1[num], end=' ')
    num += 1
print()


# Using list comprehensions

print([i for i in list1 if i % 2 == 0])

# Using filter

res = list(filter(lambda x: (x % 2 == 0), list1))
print(res)

# using recursion


def evenNumbers(li, n=0):
    if n == len(li):
        exit()
    if li[n] % 2 == 0:
        print(li[n], end=' ')

    evenNumbers(li, n+1)


evenNumbers(list1)
