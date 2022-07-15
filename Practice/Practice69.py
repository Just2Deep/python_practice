# Finding if a sum of number can be by prime numbers

def primeNumbers(n):
    prime = []
    sums = []

    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

    for idx, i in enumerate(prime):
        for j in prime[idx+1:]:
            if i + j == n:
                sums.append([i, j])

    if sums:
        return sums
    else:
        return False


print(primeNumbers(9))
