#
one = ["", "one ", "two ", "three ", "four ",
       "five ", "six ", "seven ", "eight ",
       "nine ", "ten ", "eleven ", "twelve ",
       "thirteen ", "fourteen ", "fifteen ",
       "sixteen ", "seventeen ", "eighteen ",
       "nineteen "]
# This code only the range of 0 to 100
ten = ["", "", "twenty ", "thirty ", "forty ", "fifty ",
       "sixty ", "seventy ", "eighty ", "ninety "]


def numToWords(n, s):
    str = ''
    if (n > 19) and n != 100:
        str = ten[n//10] + one[n % 10]
    elif n == 100:
        pass
    else:
        str = one[n]

    if (n):
        str += s

    return str


def convertToWords(n):
    out = ""
    out += numToWords((n // 10000000), "crore ")
    out += numToWords(((n // 100000) % 100), "lakh ")
    out += numToWords(((n // 1000) % 100), "thousand ")
    out += numToWords(((n // 100) % 10), "hundred ")
    if (n > 100 and n % 100):
        out += "and "
        out += numToWords((n % 100), "")
    elif n == 0:
        out = 'Zero'
    else:
        out += numToWords(n, "")
    return out


print(convertToWords(100))
