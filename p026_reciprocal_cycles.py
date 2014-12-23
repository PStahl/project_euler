#!/usr/bin/python

ONE = 1.0

def cycle_length(d):
    """Computes the length of the recurring cycle in the decimal representation
    of the rational number 1/d if any, 0 otherwise
    """

    if not isinstance(d, int) or d <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")

    rlist = []
    qlist_len = 0
    remainder = 1

    while remainder:
        remainder = remainder % d
        if remainder in rlist:
            return qlist_len - rlist.index(remainder)
        rlist.append(remainder)
        remainder *= 10
        qlist_len+=1

    return 0

max = 0
max_i = 0
for i in range(2, 1000):
    l = cycle_length(i)
    if l > max:
        max = l
        max_i = i

print max_i
