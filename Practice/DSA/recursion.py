# Recursion
# • Recursion is when a function calls itself.
# • Every recursive function has two cases: the base case
# and the recursive case.
# • A stack has two operations: push and pop.
# • All function calls go onto the call stack.
# • he call stack can get very large, which takes up a lot of memory.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(4))
