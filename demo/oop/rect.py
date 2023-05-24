class Rect:
    def __init__(self, length=10, width=10):
        # Object attributes 
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rect()
print(r.area())
r = Rect(20,30)
print(r.area())

