"""
common math functions to the project euler solutions
"""

import math


first_primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23]

def is_prime(n) -> bool:
    """ a prime number is only divisible by itself and 1"""
    if n in first_primes:
        return True
    for p in first_primes:
        if n % p == 0:
            return False
    for f in range(2,math.isqrt(n)):
        if n % f == 0:
            return False
    return True 


__all__ = [ "first_primes", "is_prime"]
