import re

f = open("customers.txt", "rt")
customers = {}
for line in f.readlines():
    # find name
    match = re.search("[a-zA-Z]+", line)
    if match is None:  # Name not found, so ignore
        continue

    name = match.group()

    # find mobile number
    match = re.search(r"\d+", line)
    if match is None:  # Mobile not found, so ignore
        continue

    mobile = match.group()
    if len(mobile) != 10:  # not a valid mobile number
        continue

    customers[name] = mobile

f.close()

for name, mobile in sorted(customers.items()):
    print(f"{name:20}  {mobile}")
