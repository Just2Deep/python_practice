# Finding HCF and LCM of 2 numbers;

def HCF(num1, num2):
    for i in range(1, min(num1, num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i

    return hcf


print(HCF(36, 60))


def LCM(n1, n2):
    for i in range(max(n1, n2), (n1*n2)+1):
        if i % n1 == 0 and i % n2 == 0:
            lcm = i
            break
    return lcm


print(LCM(36, 60))
