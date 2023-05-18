lst = ["abc", "xyz", "Pqr", "Def", "def", "aBc"]


for n in filter(str.islower, lst):
    print(n)
