# Python program to print all negative numbers in a range

def findNeg(start, end):
    li = []
    for i in range(start, end):
        if i < 0:
            li.append(i)

    return li


print(findNeg(-4, 6))
