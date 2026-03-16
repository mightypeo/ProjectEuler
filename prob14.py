"""
problem 14 from Project Euler

The following iterative sequence is defined for the set of positive integers:

  ( is even)
   ( is odd)
Using the rule above and starting with , we generate the following sequence:

It can be seen that this sequence (starting at  and finishing at ) contains  terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at .

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time

collatz_map = { 1: 1}

def collatz_func(n):
    global collatz_map
    
    if n in collatz_map:
        return collatz_map[n]
    if n % 2 == 0:
        x = 1 + collatz_func( int( n/2))
    else:
        x = 1 + collatz_func( int(3*n+1))
    collatz_map[n] = x
    return x

largest_so_far = 1
highest = 0
t = time.time()
for i in range(1,1000000):
    temp = collatz_func( i)
    if temp > largest_so_far:
        highest = i
        largest_so_far = temp

print 'It took {0:8.4f}s to find {1} as the largest value with a length of {2}'.format(  time.time() - t, temp, collatz_map[temp])
