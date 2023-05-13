st = "How do you do"

chars = []
for c in st:
    if c not in chars: # found first time
        print(f"{c} - {st.count(c)}")
        chars.append(c)

    