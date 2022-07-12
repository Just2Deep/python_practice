# print all even numbers in a given range

def evenNumbers(start, end):
    li = []
    for i in range(start, end+1):
        if i % 2 == 0:
            li.append(i)

    return li


print(evenNumbers(2, 16))
