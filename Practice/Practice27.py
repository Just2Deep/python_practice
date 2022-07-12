# Python program to count positive and negative numbers in a list

list1 = [2, -7, 5, -64, -14]

neg_c = []
pos_c = []
for i in list1:
    if i < 0:
        neg_c.append(i)
    else:
        pos_c.append(i)

print('Neg:', len(neg_c))
print('Pos:', len(pos_c))

# using list and lambda

negative_num = len([x for x in list1 if x < 0])
print(negative_num)

positive_num = list(filter(lambda x: (x >= 0), list1))
print(len(positive_num))
