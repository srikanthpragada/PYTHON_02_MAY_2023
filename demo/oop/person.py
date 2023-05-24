class Person:
    def __init__(self, name, age):
        # private attributes
        self.__name = name
        self.__age = age

    def show(self):
        print(self.__name)
        print(self.__age)


p = Person("Bill", 30)
p.show()
print(p.__dict__)
print(p._Person__name)
