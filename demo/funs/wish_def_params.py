def wish(person="Guest", msg='Hello'):
    print(msg, person)


# Positional Args
wish()
wish("Peter")
wish("Bill", "Hi")
wish("Hello", "Dave")

# keyword args
wish(person="Joe", msg="Good Morning")
wish(msg="Hi")

