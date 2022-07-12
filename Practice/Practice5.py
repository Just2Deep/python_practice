# Maximum of two numbers

from string import printable


a = -2
b = -3

# naive method

if a >= b:
    print(a)
else:
    print(b)

# using max func

print(max(a, b))

# using ternary operator

print(a if a >= b else b)
