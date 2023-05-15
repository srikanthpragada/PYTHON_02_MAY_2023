# Unique chars in 5 strings

names = ["abc", "bc", "de", "x", "ade"]

chars = set()
for n in names:
    chars = chars | set(n)

print(sorted(chars))


