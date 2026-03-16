#
# problem 25 of project euler
# find first 1000 digit fibonacci number

"""
The Fibonacci sequence is defined by the recurrence relation:
F(n) = F(n-1) + f(n-2) , where f(1) = 1 and f(2) = 2 .
Hence the first  terms will be:

The th term, , is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain  digits?
"""
fs = 0
f1 = 1
f2 = 1
c = 2  # we're starting with F2
while fs <= 999:
    fib = f1 + f2
    fs = len(str(fib))
    f1, f2 = f2, fib
    c = c + 1

print("F{0} which is {1} has {2} digits".format(c, fib, fs))
