# Python program to print all positive numbers in a range

def findPos(start, end):
    li = []
    for i in range(start, end+1):
        if i >= 0:
            li.append(i)

    return li


print(findPos(-4, 5))
