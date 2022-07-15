# Python – Extract words starting with K in String List

"""
Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l
Output : ['learning', 'love']
Explanation : All elements with L as starting letter are extracted.

Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = m
Output : []
Explanation : No words started from “m” hence no word extracted. 
"""
# Method 1 : Using loop + split()

# initializing list
test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "g"

res = []

for i in test_list:
    check = i.split(' ')
    for word in check:
        if word[0].lower() == K.lower():
            res.append(word)

print("The final list is : " + str(res))

# Method 2: Using list comprehensions and split()

result = [ele for sub in test_list for ele in sub.split()
          if ele[0].lower() == K.lower()]
print("The final list is : " + str(result))
