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
