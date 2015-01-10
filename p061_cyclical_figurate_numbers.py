#/usr/bin/python

from itertools import permutations

from project_euler import timeit


P3 = [n*(n+1)/2 for n in range(45, 141)]
P4 = [n*n for n in range(32, 100)]
P5 = [n*(3*n-1)/2 for n in range(26, 82)]
P6 = [n*(2*n-1) for n in range(23, 71)]
P7 = [n*(5*n-3)/2 for n in range(21, 64)]
P8 = [n*(3*n-2) for n in range(19, 59)]


ps = [P3, P4, P5, P6, P7, P8]

print P3

perms = permutations([1,2,3,4,5,6,7,8,9,0], 4)


