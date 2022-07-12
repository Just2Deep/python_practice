# Python program to check if the list contains three consecutive common numbers in Python

# creating the array
arr = [4, 5, 5, 5, 3, 8, 22, 22, 22, 5]

# size of the list
size = len(arr)

final_list = []
# looping till length - 2
for i in range(size - 2):
    if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
        final_list.append(arr[i])

print(final_list)
