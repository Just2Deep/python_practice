# Python – Remove words containing list characters

# Method 1 : Using all() + list comprehension

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# initializing char list
char_list = ['g', 'o']

# printing original list
print("The original list is : " + str(test_list))

# printing character list
print("The character list is : " + str(char_list))

res = [ele for ele in test_list if all(ch not in ele for ch in char_list)]
print('The final list is:', res)


# Method 2 brute force

result = []
flag = 1
for i in test_list:
    for letter in i:
        if letter in char_list:
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        result.append(i)

print('The final list is:', result)
