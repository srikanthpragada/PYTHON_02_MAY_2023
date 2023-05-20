g = 1000  # Global variable


def f1():
    a = 100  # enclosing
    global g
    g = 2000

    def f2():
        b = 200  # local variables
        nonlocal a
        a = 10
        print(g, a, b)

    f2()
    print(a)


f1()
