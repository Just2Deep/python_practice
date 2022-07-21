# random module

import random

value = random.random()  # random number between (0, 1]
print(value)

value2 = random.uniform(1, 10)  # random floating point number between 1 to 10
print(value2)

# use randint to simulate integers or whole numbers.
# example roll a dice

value3 = random.randint(1, 6)
print(value3)

# choice is to a random value in a list

greeting = ['Hi', 'Hello', 'Howdy', 'Hola', 'Hey']
msg = random.choice(greeting)

print(msg + ', Deep!')

# if you want the values multiple times we can use choices and to assign weights
# taking roulette example

colors = ['Red', 'Black', 'Green']

results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

# to shuffle the list we can use shuffle
# generate a deck and print a hand, which does not repeat

deck = list(range(1, 53))

random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)
print(hand)
