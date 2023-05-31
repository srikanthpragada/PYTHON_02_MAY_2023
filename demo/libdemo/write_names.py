names = ['Java', 'C#', 'Python', "JavaScript", "SQL"]

f = open("names.txt", "wt")
for n in names:
    f.write(n + "\n")

f.close()
