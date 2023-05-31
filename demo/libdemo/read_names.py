f = open("names.txt", "rt")

for n in sorted(f.readlines()):
    print(n.strip())

f.close()
