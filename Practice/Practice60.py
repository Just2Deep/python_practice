# Harshad Number

def harshad(num):
    li = [int(i) for i in str(num)]

    if num % sum(li) == 0:
        return 'Harshad'
    else:
        return 'Not Harshad'


number = 406
print(harshad(number))
