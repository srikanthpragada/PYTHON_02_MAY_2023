class Product:
    # Static attribute or class attribute
    taxrate = 18

    @staticmethod
    def settaxrate(newrate):
        Product.taxrate = newrate

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def netprice(self):
        return self.price + self.price * Product.taxrate / 100


Product.settaxrate(15)
p = Product("Product1", 10000)
#p.price = 1000
print(p.netprice())
