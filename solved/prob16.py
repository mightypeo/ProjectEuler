"""
problem 16 of Project euler

2^15 is 32768 and the sum of the digits is 3+2+7+6+8=26

What is the sum of the digits of 2^1000

the answer is 1366
"""

import math
import pytest


def sum_of_digits(i: int) -> int:
    """take the sum of the individual digits of a number"""
    num_s = str(i)
    result = 0
    for c in num_s:
        result += int(c)

    return result


@pytest.mark.parametrize("actual,expected", [(1024, 7), (32768, 26)])
def test_sum_digits(actual, expected):
    assert sum_of_digits(actual) == expected


def main():

    target = int(2 << 999)  # starting the powers a 1
    print(f"Computing the sum of the digits of {target:_d} ... ", end="")
    sum = sum_of_digits(target)
    print(f"it is {sum:5d}")


if __name__ == "__main__":
    main()
