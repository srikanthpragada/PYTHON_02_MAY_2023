l = [1, 10, 30, 40]

# i = 0
# for n in l:
#     print(i, n)
#     i += 1

# unpack tuples provided by enumerate()
for idx, value in enumerate(l, start=1):
    print(idx, value)
