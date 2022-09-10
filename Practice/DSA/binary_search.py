# binary search algorithm
# takes a sorted list and returns the index of an element in log n time
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15]


def binary_search(lists, num):
    low = 0
    high = len(lists) - 1

    while (low < high):

        mid = (low + high) // 2  # find the middle element

        if lists[mid] == num:  # if mid is the element to be found
            return mid

        elif lists[mid] > num:  # if middle is greater than element to be found
            high = mid - 1

        elif lists[mid] < num:  # if middle is lesser than element to be found
            low = mid + 1

    return -1  # if num doesnt exist


print(binary_search(nums, 15))
