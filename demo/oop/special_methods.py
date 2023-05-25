class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"{self.x},{self.y} - {self.r}"

    def __eq__(self, other):
        return self.r == other.r

    def __lt__(self, other):
        return self.r < other.r

    def __int__(self):
        return self.r


c1 = Circle(10, 10, 10)
print(int(c1))   # c1.__int__()

c2 = Circle(10, 20, 30)
c3 = Circle(10, 10, 5)

print(c1)
print(c1.__str__())
print(c1 == c3)  # c1.__eq__(c3)
# print(c2 > c1)  # c1.__gt__(c2)

l = [c1, c2, c3]
for c in sorted(l):
    print(c)

print(int(c1))  # c1.__int__()
