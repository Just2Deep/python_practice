# print all odd numbers in a given range

def oddNumbers(start, end):
    li = []
    for i in range(start, end+1):
        if i % 2 != 0:
            li.append(i)

    return li


print(oddNumbers(4, 11))
