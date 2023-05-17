def table(num: int, size: int = 10):
    for i in range(1, size + 1):
        print(f"{num:3} * {i:2} = {i * num:5}")


table(15)
table(25, 5)
