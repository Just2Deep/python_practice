# Fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    li = []
    for i in range(n):
        b = a + b
        a, b = b, a

        li.append(b)
    return li[-1]


number = 10
print(fibonacci(number))


def fibSeries(i):
    if i <= 1:
        return i
    else:
        return fibSeries(i-1) + fibSeries(i-2)


for i in range(number):
    print(fibSeries(i), end=" ")


# finding factors of a number

factors = [i for i in range(2, number) if number % i == 0]
print(factors)
