f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    name = parts[0]
    # Convert str to int and ignore non-convertible numbers
    total = sum([int(n) for n in parts if n.isdigit()])
    print(f"{name:20} {total:4}")

f.close()

f.close()
