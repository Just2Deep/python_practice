# Automorphic number

def automorphic(num):
    square = num**2

    if square % (10 ** int(len(str(num)))) == num:
        print('Automorphic')
    else:
        print('Not Automorphic')


automorphic(376)
