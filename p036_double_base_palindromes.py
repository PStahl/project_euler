#!/usr/bin/python


def is_palindrome(n):
    s = str(n)
    return all(s[i] == s[len(s) - 1 - i] for i in range(0, (len(s) / 2)))


def to_binary(n):
    return str(bin(n)).replace("0b", "")

result = sum([n for n in range(1, 1000000) if is_palindrome(n) and is_palindrome(to_binary(n))])

print result
