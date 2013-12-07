# coding: utf-8

 
from lib.mergesort import mergesort
from lib.bisect import *
 
input_array = []
 
with open('algo1_programming_prob_2sum.txt', 'r') as f:
    for line in f:
        input_array.append(int(line.rstrip()))
 
print "data loaded"
 
A = mergesort(input_array)
 
del input_array
 
print "data sorted"
 
Tees = dict()
 
for i in xrange(-10000, 10001):
    Tees[i] = 0
 
for x in A:
    lower_bound = -10000 - x
    upper_bound = 10000 - x
 
    left = bisect_left(A, lower_bound)
    right = bisect_right(A, upper_bound)
 
    for y in xrange(left, right):
        if x == A[y]:
            continue
 
        t = x + A[y]
 
        Tees[t] = 1
 
print sum(Tees.itervalues())
