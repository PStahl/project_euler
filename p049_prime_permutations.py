#!/usr/bin/python

from itertools import permutations

from project_euler import timeit, sieves, tuple_to_digit


def is_permutations(nbrs):
    perms = map(tuple_to_digit, permutations(str(nbrs[0]), 4))
    return all(nbr in perms for nbr in nbrs)


def prime_permutations():
    sieve = sieves(10000)
    diff = 3330
    for nbr in xrange(1489, 10000, 2):
        nbrs = [nbr, nbr + diff, nbr + 2 * diff]
        if all(sieve[nbr] for nbr in nbrs) and is_permutations(nbrs):
            return "".join(map(str, nbrs))


timeit(prime_permutations)
