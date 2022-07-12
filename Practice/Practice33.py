# Extract elements with Frequency greater than K


from collections import Counter
# brute force

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8, 3]
k = 3


def find_elements(lis, freq):
    res_list = list(set(lis))
    out_list = []

    for i in res_list:
        if lis.count(i) > freq:
            out_list.append(i)

    return out_list


print(find_elements(test_list, k))

# using Counter

count_list = Counter(test_list)
final_list = [key for key in count_list.keys() if count_list[key] > k]
print(final_list)
