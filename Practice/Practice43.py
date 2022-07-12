# Python – Retain records with N occurrences of K

test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2

new = []

for i in test_list:
    for ele in i:
        if ele == K:
            if i.count(K) == N and i not in new:
                new.append(i)

# Shorter way

res = [i for i in test_list if i.count(K) == N]
print(res)
print(new)

res2 = [ele for ele in test_list if sum(cnt == K for cnt in ele)]
print(res2)
