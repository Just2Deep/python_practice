# Recursion
# • Recursion is when a function calls itself.
# • Every recursive function has two cases: the base case
# and the recursive case.
# • A stack has two operations: push and pop.
# • All function calls go onto the call stack.
# • he call stack can get very large, which takes up a lot of memory.

def fact(n):
    if n == 1:  # base case
        return 1
    else:  # recursive case
        return n * fact(n-1)


print(fact(4))

# sum of elements in a array


def sum_array(arr):

    if arr == []:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])


print(sum_array([1, 2, 3, 4]))

# number of elements in a list


def num_list(arr):
    if arr == []:
        return 0
    else:
        return 1 + num_list(arr[1:])


print(num_list([-1]))

# binary search using recursion


def rec_binary(arr, high, low, ele):
    if high >= low:
        mid = (high+low) // 2

        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            return rec_binary(arr, mid - 1, low, ele)
        else:
            return rec_binary(arr, high, mid+1, ele)

    return -1


print(rec_binary([1, 2, 3, 4, 5, 6], 5, 0, 7))
