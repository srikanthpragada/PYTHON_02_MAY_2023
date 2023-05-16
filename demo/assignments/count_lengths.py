names = ['abc', 'xyz', 'ab', 'pq', 'def', 'defg']

len_dict = {}

for n in names:
    l = len(n)
    count = len_dict.get(l, 0)
    len_dict[l] = count + 1

print(len_dict)
