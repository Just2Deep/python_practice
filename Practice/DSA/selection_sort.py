# selection sort algorithm, big(O) value is N^2

def selection_sort(nums):
    sorted_list = []

    while nums != []:
        smallest = find_smallest(nums)
        sorted_list.append(nums.pop(smallest))

    return sorted_list


def find_smallest(nums):
    smallest_index = 0
    smallest_number = nums[smallest_index]

    for i in range(len(nums)):
        if nums[i] < smallest_number:
            smallest_number = nums[i]
            smallest_index = i

    return smallest_index


numbers = [5, 91, 2, 1, 21, 4, 6, 9, 5]

print(selection_sort(numbers))
