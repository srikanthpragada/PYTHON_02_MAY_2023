st = "90,45,87,93"

parts = st.split(",")
total = 0
for v in parts:
    total += int(v)

print(total)

