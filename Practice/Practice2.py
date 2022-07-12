# Python program to swap two elements in a list


from webbrowser import get


def Swap(list, pos1, pos2):

    # python swapping
    # list[pos1], list[pos2] = list[pos2], list[pos1]

    # tuple variable

    #get = list[pos1], list[pos2]
    #list[pos2], list[pos1] = get

    # using pop and inset method

    first_element = list.pop(pos1)
    second_element = list.pop(pos2-1)

    list.insert(pos2, first_element)
    list.insert(pos1, second_element)
    return list


num_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(Swap(num_list, 2, 4))
