# Highest factor other than number
num = 27
for i in range(num//2, 0, -1):
    if num % i == 0:
        print(i)
        break



