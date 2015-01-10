#!/usr/bin/python


from project_euler import timeit


def n_digit_fibo(n):
    N = 1000

    fibs = [1, 1, 2]
    i = 2
    while len(str(fibs[i])) < n:
        i += 1
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return i + 1


timeit(n_digit_fibo, 1000)
