price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

if qty >= 3:
    price = price * .70
elif qty >= 2:
    price = price * .85
else:
    price = price * .95

amount = price * qty
print(amount)
