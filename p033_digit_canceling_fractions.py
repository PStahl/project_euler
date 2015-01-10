#!/usr/bin/python

from project_euler import timeit, get_non_distinct_factors


def is_curious(n, d):
    a = [int(c) for c in str(n)]
    b = [int(c) for c in str(d)]
    val = float(n) / d
    if 0 in a or 0 in b or n == d:
        return False

    if b[0] in a:
        a.remove(b[0])
        return float(a[0]) / b[1] == val
    elif b[1] in a:
        a.remove(b[1])
        return float(a[0]) / b[0] == val
    else:
        return False


def cancelling_fractions():
    curious = [(a, b) for a in range(10, 100) for b in range(10, 100) if a < b and is_curious(a, b)]

    n = reduce(lambda x, y: x * y, [a for (a, b) in curious])
    d = reduce(lambda x, y: x * y, [b for (a, b) in curious])
    n = get_non_distinct_factors(n) 
    d = get_non_distinct_factors(d) 
    common = list(set(n) & set(d))

    i = 0
    while i < len(d):
        if d[i] in n:
            n.remove(d[i])
            d.remove(d[i])
        else:
            i += 1

    d = reduce(lambda x, y: x * y, d)
    
    return d


timeit(cancelling_fractions)
