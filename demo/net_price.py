# Take price and calculate netprice with 10% discount

data = input("Enter price :")
price = int(data)  # convert str to int
discount = price * 10 // 100   # calculate discount @ 10%
net_price = price - discount
print(net_price)


