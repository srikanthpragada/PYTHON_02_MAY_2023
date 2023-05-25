class Person:
    def __init__(self, name, age):
        # private attributes
        self.__name = name
        self.__age = age

    def show(self):
        print(self.__name)
        print(self.__age)

    @property
    def category(self):
        if self.__age < 20:
            return "Young"
        elif self.__age < 50:
            return "Middle-aged"
        else:
            return "Matured"


p = Person("Bill", 30)
print(p.category)

p.show()
print(p.__dict__)
print(p._Person__name)
