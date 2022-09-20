# quicksort
# • D&C works by breaking a problem down into smaller and smaller
# pieces. If you’re using D&C on a list, the base case is probably an
# empty array or an array with one element.
# • If you’re implementing quicksort, choose a random element as the
# pivot. he average runtime of quicksort is O(n log n)!
# • the constant in Big O notation can matter sometimes. hat’s why
# quicksort is faster than merge sort.
# • the constant almost never matters for simple search versus binary
# search, because O(log n) is so much faster than O(n) when your list
# gets big

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lower = [i for i in arr[1:] if i < pivot]
        higher = [i for i in arr[1:] if i > pivot]

        return quick_sort(lower) + [pivot] + quick_sort(higher)


print(quick_sort([9, 3, 6, 1, 2, 7, -2, -5]))
