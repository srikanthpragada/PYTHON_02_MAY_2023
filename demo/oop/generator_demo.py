def numbers():
    for n in range(1, 6):
        yield n


g = numbers()

print(type(g))
print(next(g))  # 1
print(next(g))  # 2

for n in numbers():
    print(n)