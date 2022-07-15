# Python – Prefix frequency in string List

# Method 1: using loop and startswith

# Initializing list
test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
test_sub = 'gfg'

res = 0

for i in test_list:
    if i.startswith(test_sub):
        res += 1

print('Strings count with matching frequency :', res)

# Method 2 : Using sum() + startswith()

# Prefix frequency in List
# using sum() + startswith()
res = sum(sub.startswith(test_sub) for sub in test_list)

# printing result
print("Strings count with matching frequency :", res)
