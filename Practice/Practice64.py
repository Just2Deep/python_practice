# calculating decimal from binary


def calDecimal(n):
    base = 1
    value = 0
    while n > 0:
        rem = n % 10
        value = value + rem * base
        n = n//10
        base *= 2

    return value


print(calDecimal(1101))


def calBinary(n):
    base = 1
    value = 0

    while n > 0:
        rem = n % 2
        value = value + rem * base
        base = base * 10
        n //= 2

    return value


print(calBinary(14))

n = 14
new = []
while (n > 0):
    new.append(str(n % 2))
    n //= 2

print(''.join((new[::-1])))
