#!/usr/bin/python

import itertools

test_N = 5
test_nbrs = ['0', '1', '2']
test_permutations = itertools.permutations(test_nbrs)
#print list(test_permutations)

N = 1000000
nbrs = [str(unichr(x + ord('0'))) for x in range(0, 10)]
permutations = itertools.permutations(nbrs)
print list(permutations)[N - 1]

