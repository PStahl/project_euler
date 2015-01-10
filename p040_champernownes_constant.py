#!/usr/bin/python

from project_euler import timeit


def champernownes_constant(upper_limit):
    """Champernowne's constant = 0.12345678910111213...
    Dn = nth digit of the fractional part.
    D12 = 1.

    Find D1 * D10 * D100 * ... * Dupper_limit
    """
    index = 0
    current_nbr = 1
    next_index = 1
    result = []

    while index <= upper_limit:
        s = str(current_nbr)
        length_of_current = len(s)

        if index % next_index == 0:
            result.append(current_nbr)
            next_index = next_index * 10
        elif (index + length_of_current) % next_index < length_of_current:
            diff = next_index - index
            result.append(int(s[diff - 1]))
            s = s[diff:]
            index = next_index
            next_index = next_index * 10

        index += len(s)
        current_nbr += 1

    return reduce(lambda x, y: x * y, result)


timeit(champernownes_constant, 1000000)
