# Avg. Length of the strings

total_len = count = 0
while True:
    name = input("Enter name [end to stop] :")
    if name.upper() == 'END':
        break

    total_len += len(name)
    count += 1

print(f"Avg Length = {total_len/count:5.2f}")

