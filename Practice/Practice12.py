# Finding sum and average of a list in python

# Naive Method

L = [4, 5, 1, 2, 9, 7, 10, 8]
count = 0

for i, value in enumerate(L):

    count += value


print(f'The Sum of list is {count}, The Average of list is {count/len(L)}')

# Using SUM method

#count = sum(L)
print(f'The Sum of list is {sum(L)}, The Average of list is {sum(L)/len(L)}')
