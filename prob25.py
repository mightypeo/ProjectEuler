#
# problem 25 of project euler
# find first 1000 digit fibonacci number

fs = 0
f1 = 1
f2 = 1
c = 2   # we're starting with F2
while fs <= 999:
    fib = f1 + f2
    fs = len(str(fib))
    f1, f2 = f2, fib
    c = c + 1
    
print( 'F{0} which is {1} has {2} digits'.format( c, fib, fs))
