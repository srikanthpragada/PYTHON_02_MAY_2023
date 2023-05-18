lst = [1, 2, 4, 5, 8]


def iseven(n):
    return n % 2 == 0


for n in filter(iseven, lst):
    print(n)
