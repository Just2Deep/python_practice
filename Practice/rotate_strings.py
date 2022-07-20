# rotating string for n elements (both right and left)

def num_of_rotations(word, n):
    # if number is rotations is greater use mod to make it below len of string
    if n > len(word):
        rotation = n % len(word)
    else:
        rotation = n

    return rotation


def left_rotate(word, n):
    rotation = num_of_rotations(word, n)

    # splitting string in 2 parts based on rotation number
    first_part = word[:rotation]
    second_part = word[rotation:]

    return second_part + first_part


def right_rotate(word, n):
    rotation = num_of_rotations(word, n)

    # splitting string in 2 parts based on rotation number

    first_part = word[:len(word)-rotation]
    second_part = word[len(word)-rotation:]

    return second_part + first_part


word = 'pythonprogram'
n = 15

print(left_rotate(word, n))
print(right_rotate(word, n))
