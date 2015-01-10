#!/usr/bin/python

from project_euler import timeit, is_palindrome


def to_binary(n):
    return str(bin(n)).replace("0b", "")


def double_base_palindromes(n):
    return sum([n for n in range(1, n) if is_palindrome(n) and is_palindrome(to_binary(n))])


timeit(double_base_palindromes, 1000000)
