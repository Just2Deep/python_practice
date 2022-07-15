# Swapping first and last element in a list

from numpy import linspace


def swapList(new_list):

    size = len(new_list)

    # swapping
    #new_list[0], new_list[-1] = new_list[-1], new_list[0]
    get = new_list[0], new_list[-1]

    new_list[-1], new_list[0] = get

    return new_list


list_num = [1, 2, 3, 5, 7, 9]

print(swapList(list_num))

""" Other methods to solve the same
1. We can use temp variable for swapping 

2. we can use args passing 
    start, *middle, last = new_list
    new_list = [end, *middle , start]

3. We can use pop and insert 
    start = list.pop(0)
    end = list.pop(-1)
    list.insert(0 , end)
    list.append(start)

4. Using tuple variable
    get = list[0], list[-1]

    list[-1], list[0] = get

"""
