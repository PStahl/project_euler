#!/usr/bin/python

from project_euler import timeit


def term(n):
    return n * (n + 1) / 2


def word_value(word):
    return sum([ord(c) - ord('A') + 1 for c in word])


def coded_triangle_numbers(filename):
    with open(filename, 'r') as f:
        words = f.read().split(",")
        words = [word.strip('\"') for word in words]

        N = max([len(word) for word in words])
        triangular = set([term(n) for n in range(1, 2 * N)])

        return len([word_value(word) for word in words if sum([ord(c) - ord('A') + 1 for c in word]) in triangular])


timeit(coded_triangle_numbers, 'p042_words.txt')
