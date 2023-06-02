import os


allfiles = os.walk(r"d:\classroom\may2\demo")

for (dirname, folders, files) in allfiles:
    print(f"{dirname:20}  {len(files):3}")

    