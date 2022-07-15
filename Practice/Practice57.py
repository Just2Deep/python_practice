# If given number is a strong number

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    return fact


def StrongNumber(number):
    lis = []
    for i in str(number):
        lis.append(factorial(int(i)))

    if sum(lis) == number:
        return 'Strong Number'
    else:
        return 'Not a strong number'


number = 145
print(StrongNumber(number))
