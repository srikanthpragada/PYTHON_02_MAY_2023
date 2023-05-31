f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    name = parts[0]
    total = sum(map(int, parts[1:]))
    print(f"{name:20} {total:4}")

f.close()

f.close()
