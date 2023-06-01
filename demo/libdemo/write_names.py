names = ['Java', 'C#', 'Python', "JavaScript", "SQL"]

with open("names.txt", "wt") as f:
    for n in names:
        f.write(n + "\n")

