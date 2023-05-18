lst = ["abc", "xyz", "Pqr", "Def", "def", "aBc"]


def hasupper(s: str) -> bool:
    for c in s:
        if c.isupper():
            return True

    return False


for n in filter(hasupper, lst):
    print(n)
