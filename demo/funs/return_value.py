def iseven(n: int) -> bool:
    return n % 2 == 0


def get_upper_count(s: str) -> int:
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


print(get_upper_count('HeLLo'))
