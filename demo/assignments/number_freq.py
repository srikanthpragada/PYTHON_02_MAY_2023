nums = [10, 10, 20, 40, 50, 40, 50, 20, 30]

freq = {}  # empty dict
for n in nums:
    if n in freq:  # number is found
        freq[n] = freq[n] + 1
    else:  # new number
        freq[n] = 1

for n, c in freq.items():
    print(n, c)
