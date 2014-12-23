#!/usr/bin/python

poker_hands = open("p054_poker.txt", "r").readlines()

from collections import Counter

values = {'1':1,
          '2':2,
          '3':3,
          '4':4,
          '5':5,
          '6':6,
          '7':7,
          '8':8,
          '9':9,
          '10':10,
          'J':11,
          'Q':12,
          'K':13,
          'A':14}

def convert_hand(hand):
    return map(lambda h: (values[h[:-1]], h[-1]), hand)




def royal_flush(h1):
    return (all(i in [c for c in [10, 11, 12, 13, 14]] for i in [h[0] for h in h1]) and
            flush(h1))

def straight_flush(h1):
    return straight(h1) and flush(h1)


def four_of_a_kind(h1):
    values = [c[0] for c in h1]
    return 4 in Counter(values).values()

def full_house(h1):
    return three_of_a_kind(h1) and pair(h1)

def flush(h1):
    suit = h1[0][1]
    return all(c[1] == suit for c in h1)

def straight(h1):
    values = sorted([c[0] for c in h1])
    return values[0] + 4 == values[-1]

def three_of_a_kind(h1):
    values = [c[0] for c in h1]
    return 3 in Counter(values).values()

def two_pair(h1):
    values = [c[0] for c in h1]
    return Counter(values).values().count(2) == 2

def pair(h1):
    values = [c[0] for c in h1]
    return (Counter(values).values().count(2) == 1

def high_card(h1):
    values = [c[0] for c in h1]
    return (True, max(values))


ranks = [royal_flush,
         straight_flush,
         four_of_a_kind,
         full_house,
         flush,
         straight,
         three_of_a_kind,
         two_pair,
         pair,
         high_card]

def compare_hands(h1, h2):
    h1 = convert_hand(h1)
    h2 = convert_hand(h2)

    for f in ranks:
        (v1, r1) = f(h1)
        (v2, r2) = f(h2)
        if v1 and not v2:
            return 1
        elif not v1 and v2:
            return 0
        elif v1 and v2:
            return 0

    return 0

test_royal = convert_hand("10C JC QC KC AC".split())
test_four = convert_hand("10C 10C QC 10C 10C".split())
test_full_house = convert_hand("10C QC QC QC 10C".split())
test_three = convert_hand("10C 10C QC 10C AC".split())
test_two_pair = convert_hand("KC KC QC 10C 10C".split())
test_pair = convert_hand("KC AC QC 10C 10C".split())
print royal_flush(test_royal)
print straight_flush(test_royal)
print four_of_a_kind(test_four)
print full_house(test_full_house)
print three_of_a_kind(test_three)
print two_pair(test_two_pair)
print pair(test_pair)

result = [compare_hands(line.split()[0:5], line.split()[5:]) for line in poker_hands]
print result
