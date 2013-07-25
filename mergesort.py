# coding: utf-8
# Author: Jerry Rong

"""
Implementation of merge sort
"""

def merge_sort(a):
    """(list) -> NoneType

    return an already sorted array
    """
    # base case
    length = len(a)
    if length == 1:
        return
    left_half  = a[:length/2]
    right_half = a[length/2:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge_split(a, left_half, right_half)


def merge_split(a, left, right):
    """(list, list, list) -> NoneType
    """
    i = 0
    j = 0
    left_size = len(left)
    right_size = len(right)
    for k in range(len(a)):
        if i >= left_size:
            a[k] = right[j]
            j += 1
        elif j >= right_size:
            a[k] = left[i]
            i += 1
        elif left[i] > right[j]:
            a[k] = right[j]
            j += 1
        else:
            a[k] = left[i]
            i += 1

