def find_digit_pos(st):
    for idx, c in enumerate(st):
        if c.isdigit():
            return idx

    return -1


print(find_digit_pos('abc'))
print(find_digit_pos('abc123xyz987'))
