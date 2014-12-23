#!/usr/bin/python

import math

def divisors(n):
    yield 1

    largest = int(math.sqrt(n))

    # special-case square numbers to avoid yielding the same divisor twice
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i

def is_abundant(n):
    if n < 12:
        return False
    return sum(divisors(n)) > n

def is_abundant_sum(n):
   for i in abundants:
       if i > n:  # assume "abundants" is ordered
         return False
       if (n - i) in abundants_set:
           return True
   return False

UPPER_LIMIT = 28123

abundants = [n for n in range(1, UPPER_LIMIT) if is_abundant(n)]
abundants_set = set(abundants)

sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))

print sum_of_non_abundants
