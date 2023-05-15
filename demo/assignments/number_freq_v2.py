nums = [10, 10, 20, 40, 50, 40, 50, 20, 30]

freq = {}  # empty dict
for n in set(nums):
    freq[n] = nums.count(n)

for n, c in sorted(freq.items()):
    print(n, c)
