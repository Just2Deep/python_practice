# Sum of digits in a number

number = 123
digits = []

for i in str(number):
    digits.append(int(i))

print(sum(digits))

# reverse a number


reverse = int(str(number)[::-1])
print(reverse)

# palindrome number
rev = 0
num = 1321
check = num
while (num > 0):
    rem = num % 10
    num = num//10

    rev = rev*10 + rem

if check == rev:
    print('True')
else:
    print('False')
