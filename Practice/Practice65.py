# converting all 0's in a number to 1

num = 200234
a = []
for i in str(num):
    if int(i) == 0:
        a.append('1')
    else:
        a.append(i)

b = ''.join(a)
print(int(b))
