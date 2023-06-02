import os

allfiles = os.walk(r"d:\classroom\may2\demo")
count = 0
for (dirname, folders, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
            count += 1

print("Count = ", count)
