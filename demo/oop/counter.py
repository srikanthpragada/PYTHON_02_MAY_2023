class Counter:
    # Constructor
    def __init__(self):
        # Object attribute
        self.value = 0

    # Methods
    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def getvalue(self):
        return self.value


c1 = Counter()  #  __init__()
c1.inc()
c1.inc()
print(c1.getvalue())
