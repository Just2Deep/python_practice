# Swap elements in string list

# Swap elements in String list
# using replace() + list comprehension

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# Printing original list
print(test_list)

# swapping
new_list = [sub.replace('G', '_').replace('e', 'G').replace('_', 'e')
            for sub in test_list]

print(new_list)


# Method 2 join and replace commands

# print test string

print('Original string: ' + str(test_list))

method2_list = ' '.join(test_list)
method2_list = method2_list.replace(
    'G', '_').replace('e', 'G').replace('_', 'e')

method2_list = method2_list.split(' ')
print(f'List after performing swap: {method2_list}')
