
st = "AB18843"
code = st[:2]
price = st[2:]

if code.isalpha() and price.isdigit():
    print(code, price)
else:
    print("Invalid code")