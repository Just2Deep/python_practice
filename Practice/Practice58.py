# Finding perfect number

def PerfectNumber(num):

    data = [i for i in range(1, num) if num % i == 0]
    if sum(data) == num:
        return 'Perfect'
    else:
        return 'Not Perfect'


num = 29
print(PerfectNumber(num))
