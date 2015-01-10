#/usr/bin/python

from project_euler import timeit, is_palindrome

cache = {}


def lychrel(n):
    new_n = n + int(''.join(reversed(str(n))))
    return is_lychrel(new_n, 0)


def is_lychrel(n, cnt):
    if cnt > 50:
        return True
    elif is_palindrome(n):
        return False

    if n in cache:
        return cache[n]

    n += int(''.join(reversed(str(n))))
    return is_lychrel(n, cnt + 1)


def lychrel_numbers(upper_limit):
    result = [n for n in range(upper_limit + 1) if lychrel(n)]
    return len(result)


timeit(lychrel_numbers, 10000)

