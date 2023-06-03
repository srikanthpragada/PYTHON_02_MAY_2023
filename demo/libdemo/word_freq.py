import re

with open("test.txt", "rt") as f:
    contents = f.read()

words = re.findall(r"\w+", contents)

freq = {}
for w in set(words):
    freq[w] = words.count(w)

print(freq)
