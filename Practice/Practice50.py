# Python – Split Strings on Prefix Occurrence
"""
Input : test_list = [“geeksforgeeks”, “best”, “geeks”, “and”], pref = “geek” 
Output : [['geeksforgeeks', 'best'], ['geeks', 'and']] 
Explanation : At occurrence of string “geeks” split is performed.

Input : test_list = [“good”, “fruits”, “goodness”, “spreading”], pref = “good” 
Output : [['good', 'fruits'], ['goodness', 'spreading']] 
Explanation : At occurrence of string “good” split is performed. 
"""

# Method 1 : Using loop + startswith()

# initializing list
test_list = ["geeksforgeeks", "best", "geeks", "and", "geeks", "love", "CS"]

# printing original list
print("The original list is : " + str(test_list))

# initializing prefix
pref = "geek"

res = []

for i in test_list:
    if i.startswith(pref):
        res.append([i])
    else:
        res[-1].append(i)

print('The final list is:', res)
