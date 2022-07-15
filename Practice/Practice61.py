# Abundant number

def abundant(num):

    factors = [i for i in range(1, num) if num % i == 0]

    if sum(factors) > num:
        return 'Abundant'
    else:
        return 'Not Abundant'


print(abundant(12))
