# Take price and calculate netprice with 10% discount

data = input("Enter price :")
price = float(data)  # convert str to int
discount = price * 10 / 100  # calculate discount @ 10%
net_price = price - discount

print(f'Price      {price:8.2f}')
print(f'Discount   {discount:8.2f}')
print(f'Net Price  {net_price:8.2f}')
