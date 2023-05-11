names = []  # empty list
while True:
    name = input("Enter name [end to stop] :")
    if name.upper() == 'END':
        break

    names.append(name)

for n in sorted(names):
    print(n)
