# finding the sum of fractions:

num1 = 3
den1 = 10
num2 = 4
den2 = 15


def sumFraction(n1, d1, n2, d2):
    n3 = n1*d2 + n2*d1
    d3 = d1*d2

    for i in range(1, min(n3, d3)):
        if n3 % i == d3 % i == 0:
            hcf = i

    print(f'Sum of numbers is : {n1}/{d1} + {n2}/{d2} = {n3//hcf}/{d3//hcf}')


sumFraction(num1, den1, num2, den2)
