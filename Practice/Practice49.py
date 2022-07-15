# Python – Split String of list on K character

# Method 1 : Using loop + split()

# Initializing list
test_list = ['Gfg is best', 'for Geeks', 'Preparing']

# printing original list
print("The original list is : " + str(test_list))

K = ' '

# Split String of list on K character
# using loop + split()
res = []
for i in test_list:
    for word in i.split(K):
        res.append(word)

print('The final list is:', res)

new = []
for words in test_list:
    sub = words.split(K)
    new.extend(sub)

print('The final list is:', new)


# Method 2 : Using join() + split()

string_new = K.join(test_list).split(K)

print('The final list is:', string_new)
