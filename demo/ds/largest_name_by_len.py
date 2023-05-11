# Take names and display largest name
largest = ''
while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break
   
    if len(name) > len(largest):
        largest = name

print(f"Largest name = {largest}")

