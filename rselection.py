# coding: utf-8
# Author: Jerry Rong

"""
Implementation of randomized selection algorithm
"""
import random

def rselect(a, n, i):
    """(list, int, int) -> int
    """
    if n == 1 
        return a[0]

    j = p = random.randint(0, len(a) - 1)

    if j == i:
        return p
    elif j > i:
        return rselect(a, j - 1, i)
    else:
        return rselect(a, n - j - 1, i - j - 1)
