f = open("marks.txt", "rt")
ef = open("marks_errors.txt", "wt")

for line in f.readlines():
    try:
        parts = line.strip().split(",")
        name = parts[0]
        total = sum(map(int, parts[1:]))
        print(f"{name:20} {total:4}")
    except Exception:
        ef.write(line)

f.close()
ef.close()

f.close()
