with (open("names.txt", "rt") as f1,
      open("newnames.txt", "rt") as f2):
    lines1 = set(f1.readlines())
    lines2 = set(f2.readlines())

    for line in lines1 | lines2:
        print(line.strip())
