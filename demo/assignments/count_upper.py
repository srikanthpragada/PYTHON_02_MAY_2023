# Count uppercase letters
st = "How Do you DO"
count = 0
for c in st:
    if c.isupper():
        count += 1

print(count)

