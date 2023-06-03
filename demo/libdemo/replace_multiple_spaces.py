import re

with open("test.txt", "rt") as f:
    contents = f.read()

# replace multiple spaces with one
contents = re.sub(' +', ' ', contents)

# replace multiple newslines with one
contents = re.sub('\n+', '\n', contents)

with open("test.txt", "wt") as f:
    f.write(contents)
