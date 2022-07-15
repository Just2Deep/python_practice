# Python program to Replace all Characters of a List Except the given character
"""
Input : test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T'], repl_chr = '*', ret_chr = 'G' 
Output : ['G', '*', 'G', '*', '*', '*', '*', '*', '*'] 
Explanation : All characters except G replaced by *

Input : test_list = ['G', 'F', 'G', 'B', 'E', 'S', 'T'], repl_chr = '*', ret_chr = 'G' 
Output : ['G', '*', 'G', '*', '*', '*', '*'] 
Explanation : All characters except G replaced by * 
"""
# Method 1 : Using list comprehension + conditional expressions

test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']

# printing original list
print("The original list : " + str(test_list))

# initializing repl_chr
repl_chr = '$'

# initializing retain chararter
ret_chr = 'G'

final_list = [ele if ele == ret_chr else repl_chr for ele in test_list]

print("List after replacement : ", final_list)

# Method 2 : Using map() + lambda

from_map = list(map(lambda x: ret_chr if x ==
                ret_chr else repl_chr, test_list))

print("List after replacement : ", from_map)
