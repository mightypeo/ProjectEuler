"""
problem 30 of project euler

Surprisingly ther are only three numbers that can be written as the sum of fourth powers of their digits

    1634 = 1^4 + 6^4 + 3^4 + 4^6
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included

The sum of these numbers i 1634 + 8208 + 9474 = 19316

Find the sum of all numbers that can be writte, as the sum of fifth powers of their digit


"""

import pytest


def make_power_string(number: int, power: int) -> str:
    return " + ".join([f"{c}^{power}" for c in str(number)])


def explain_power_string(number: int, power: int) -> str:
    return " = ".join(
        [
            make_power_string(number, power),
            " + ".join([f"{int(c)**power:_d}" for c in str(number)]),
        ]
    )


def sum_polynomial(number: int, power: int) -> int:
    """
    creates a sum of polynomial with digits to the power of power
    """
    factors = [int(c) ** power for c in str(number)]
    return sum(factors)


@pytest.mark.parametrize(
    "actual,expected",
    [
        (1634, "1^4 + 6^4 + 3^4 + 4^4"),
        (8208, "8^4 + 2^4 + 0^4 + 8^4"),
        (9474, "9^4 + 4^4 + 7^4 + 4^4"),
    ],
)
def test_make_power_string(actual, expected):
    assert make_power_string(actual, 4) == expected


@pytest.mark.parametrize(
    "actual,factor,success",
    [(1634, 4, True), (8208, 4, True), (9474, 4, True), (1024, 4, False)],
)
def test_sum_polynomial(actual, factor, success):
    if success:
        assert sum_polynomial(actual, factor) == actual
    else:
        assert sum_polynomial(actual, factor) != actual


def is_sum_of_factor_powers(number: int, factor) -> bool:
    sum = sum_polynomial(number, factor)
    return (sum == number, sum)


def brute_force():
    factor = 5
    numbers = []
    for i in range(1000, 10000):
        (success, single_number) = is_sum_of_factor_powers(i, factor)
        if success:
            print(
                f"{i:5d} is the sum {single_number:5d} of the its digits to the fifth power {explain_power_string(i, 5)}"
            )
            numbers.append(single_number)

    print( f"{len(numbers):4d} number found")
    print( "\n".join( [f"{n:6d}" for n in numbers]))
    print( f"{'=' * 10}")
    print( f"{sum(numbers):8d}")



def main():
    brute_force()


if __name__ == "__main__":
    main()
