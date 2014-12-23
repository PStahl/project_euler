#!/usr/bin/python

import sys

from project_euler import timeit, is_palindrome, is_palindrome_2


def largest_palindrome(palindrome_checker):
    max_so_far =  -sys.maxint
    for i in range(100, 1000):
        for j in range(100, 1000):
            if palindrome_checker(i * j):
                max_so_far = max(i * j, max_so_far)

    return max_so_far


timeit(largest_palindrome, is_palindrome)
timeit(largest_palindrome, is_palindrome_2)
