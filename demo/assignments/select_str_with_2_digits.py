data = ["abc", "1234", "xyz123", "def1", "pqr3"]


def has_2_digts(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count >= 2


for v in filter(has_2_digts, data):
    print(v)
