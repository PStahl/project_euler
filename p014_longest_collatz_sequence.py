#!/usr/bin/python

from project_euler import timeit


def longest_chain(n):
    start = 0
    seq_length = 0

    cache = [-1] * n
    for i in range(2, n):
        seq = i
        k = 0
        while not seq == 1 and seq >= i:
            k += 1
            if seq % 2 == 0:
                seq = seq / 2
            else:
                seq = seq * 3 + 1
        cache[i] = k + cache[seq]


        if cache[i] > seq_length:
            seq_length = cache[i]
            start = i
    
    return start


timeit(longest_chain, 1000000)
