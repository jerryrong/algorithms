# coding: utf-8
# Author: Jerry Rong

"""
Implementation of quick sort , use random pivot
"""

import random

def quick_sort(a, lo, hi):
    """(list, int, int) -> NoneType
    """
    
    if lo >= hi:
        return

    random_index = random.randint(lo, hi)
    a[lo], a[random_index] = a[random_index], a[lo]

    p = partition(a, lo, hi)
    quick_sort(a, lo, p - 1)
    quick_sort(a, p + 1, hi)

def partition(a, lo, hi):
    """
    """

    p = a[lo]

    i = j = lo + 1

    while j <= hi:
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1

    a[lo], a[i-1] = a[i-1], a[lo]
    return i-1
