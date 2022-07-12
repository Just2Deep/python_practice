# Python program to count Even and Odd numbers in a List

li = [2, 7, 5, 64, 14, 31, 65, 11, 4]


def Counting(lis):
    even, odd = 0, 0
    for i in lis:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)


print('Even: ' + str(Counting(li)[0]) + ' Odd: ' + str(Counting(li)[1]))


# using while loop

j = 0
even_count = 0
odd_count = 0

while(j < len(li)):
    if li[j] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    j += 1

print('Even:', even_count)
print('Odd:', odd_count)

# lambda

odd_c = list(filter(lambda x: (x % 2 != 0), li))
odd_c = len(odd_c)
print('Odd:', odd_c)

even_c = len(list(filter(lambda x: (x % 2 == 0), li)))
print('Even:', even_c)


print('Even:', len([x for x in li if x % 2 == 0]))
print('Odd:', len([x for x in li if x % 2 != 0]))
