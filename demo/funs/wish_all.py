def wish(*names, msg="Hello"):
    for n in names:
        print(msg, n)


wish("Ben", "Kevin", msg="Hi")
wish("Ben", "Kevin", "Scott")
