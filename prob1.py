"""
problem 1 from Project Euler

If we list all the natural numbers below 10 that are multiples of 3 or 2 , we get 3,5,6 and 9. The sum of these multiples is 23

Find the sum of all the multiples of  3 or 5 below 1000.

The answer will be 233168
"""


def main():
    sum = 0
    factor =3
    max_range = int(1000/factor)
    for m in range(1, max_range):
        if m % 5 == 0:
            continue
        sum += m * 3

    factor = 5
    max_range = int(1000/factor)
    for m in range(1, max_range):
        sum += m * 5

    print(f"the sum is {sum:10d}")


if __name__ == "__main__":
    main()
