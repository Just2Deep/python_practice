# Python Program to Sort the list according to the column using lambda

array = [['java', 1995], ['c++', 1983], ['python', 1989]]
res = []


def ArraySort(arr):
    for i in range(len(arr[0])):
        new = sorted(arr, key=lambda x: x[i])
        res.append(new)
    return res


a = ArraySort(array)

for i, val in enumerate(a):
    print(i, val)
