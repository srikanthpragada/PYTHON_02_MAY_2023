# Take price and calculate netprice with 10% discount

data = input("Enter price :")

price = float(data)  # convert str to int
discount = price * 10 / 100  # calculate discount @ 10%
price_after_discount = price - discount
tax = price_after_discount * 12 / 100
net_price = price_after_discount + tax

print(f'Price            {price:8.2f}')
print(f'- Discount       {discount:8.2f}')
print(f'After Discount   {price_after_discount:8.2f}')
print(f'+ Tax            {tax:8.2f}')
print(f'Net Price        {net_price:8.2f}')
