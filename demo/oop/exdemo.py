l = ["1", "x", "2", "3", "a"]

total = 0
for p in l:
    try:
        total += int(p)
    except ValueError as ex:
        print("Error : " + str(ex))

print(total)