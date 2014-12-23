#!/usr/bin/python

from collections import Counter
from itertools import permutations

def d_n(nbr, n):
    return 100*int(nbr[n-1]) + 10*int(nbr[n]) + int(nbr[n+1])

primes = [1, 2, 3, 5, 7, 11, 13, 17]

result = []
for nbr in filter(lambda x: x[3] % 2 == 0, permutations(range(10), 10)):
    if all(d_n(nbr, n) % primes[n-1] == 0 for n in range(1,9)):
        result.append(nbr)

result = map(lambda t: reduce(lambda x,y: int(str(x)+str(y)), t), result)
print sum(result)


