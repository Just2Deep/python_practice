# Python – Remove Consecutive k element records

# Method 1 : Using zip() + list comprehension

test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
k = 6

result = [idx for idx in test_list if (k, k) not in zip(idx, idx[1:])]
#print([i for i in zip((4, 5, 6, 3), (5, 6, 3))])
print(result)

# Method 2 : using any

res = [idx for idx in test_list if not any(
    idx[j] == k and idx[j + 1] == k for j in range(len(idx) - 1))]

print(res)
