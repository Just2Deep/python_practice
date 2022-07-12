#  Remove empty tuples from a list

tup = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
       ('krishna', 'akbar', '45'), ('', ''), ()]


def RemoveTuples(tup):

    new = [x for x in tup if x]
    return new


print(RemoveTuples(tup))

# using filter

tup2 = list(filter(None, tup))
print(tup2)

# using len()
for i in tup:
    if len(i) == 0:
        tup.remove(i)
print(tup)
