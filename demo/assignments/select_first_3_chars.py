data = ["ab", "1234", "xyz123", "def1", "pqr3"]


def first3(s):
    return s[:3]


for v in map(first3, data):
    print(v)
