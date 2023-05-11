# Take names and display largest name
largest = ''
while True:
    name = input("Enter name [end to stop] :")
    if name.upper() == 'END':
        break

    if name > largest:
        largest = name

print(f"Largest name = {largest}")

