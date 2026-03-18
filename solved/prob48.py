"""

problem 48 of Project Euler

The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317

find the last ten digits of the power seriec 1^1 + 2^2 ,, + 1000^1000

the answer is 9110846700

"""

powers = {1: 1}
sum = 0
for i in range(1, 1000):
    powers[i] = i**i
    print("{0}^{0} = {1}".format(i, powers[i]))
    sum += powers[i]

ssum = str(sum)
print("The last 10 digits of the power sum from 1..1000 are {0}".format(ssum[-10:]))
