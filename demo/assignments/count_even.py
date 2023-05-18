# Count uppercase letters
def count_even(lst):
    count = 0
    for v in lst:
        if v % 2 == 0:
            count += 1

    return count


print(count_even((1, 9, 5, 11)))
print(count_even([1, 9, 5, 11, 12, 20]))
