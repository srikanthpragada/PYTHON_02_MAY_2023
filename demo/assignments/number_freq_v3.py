nums = [10, 10, 20, 40, 50, 40, 50, 20, 30]

freq = {}  # empty dict
for n in nums:
    c = freq.get(n, 0)
    freq[n] = c + 1

for n, c in freq.items():
    print(n, c)
