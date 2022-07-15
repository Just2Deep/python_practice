# Armstrong number

number = 372
new = []

low = 370
high = 380

for number in range(low, high+1):
    new = []
    for i in str(number):
        new.append(int(i))

    total = sum(map(lambda x: x**len(new), new))

    if total == number:
        print('Armstrong Number', number)
    else:
        print('Not a Armstrong Number', number)
