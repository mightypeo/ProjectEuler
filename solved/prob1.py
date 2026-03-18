"""
problem 1 from Project Euler

If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3,5,6 and 9.
The sum of these multiples is 23

Find the sum of all the multiples of  3 or 5 below 1000.

The answer will be 233168
"""

ANSWER = 233168


def main():
    answer = sum([x * 3 for x in range(1, 334) if x % 5 != 0]) + sum(
        [x * 5 for x in range(1, 200)]
    )

    print(f"the sum is {answer:10d} - the correct answer is {ANSWER:10d}")


if __name__ == "__main__":
    main()
