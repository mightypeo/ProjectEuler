# problem 4 from project euler

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is   .

Find the largest palindrome made from the product of two -digit numbers."""

import pytest

ANSWER = 906609


def is_palindrome(x: int) -> bool:
    "Check to see if number is palindrome"

    xs = str(x)
    l = int(len(xs) / 2)
    for i in range(0, l):
        if xs[i] != xs[-(i + 1)]:
            return False
    return True


@pytest.mark.parametrize(
    "actual,expected", [("123321", True), (1234321, True), (123123, False)]
)
def test_is_palindrome(actual, expected):
    if expected:
        assert is_palindrome(actual)
        return
    assert not is_palindrome(actual)

products : list[tuple[int, int, int]]
def a_generator(upper: int, lower: int):
    products = [
        (a * b, a, b) for a in range(upper, lower, -1) for b in range(upper, a-1, -1)
    ]
    for p in sorted(products, key=lambda x: x[0], reverse=True):
        yield p


def find_palindrome(digits: int = 3):
    """product is commutative - not need to iterate b over the whole range"""
    lower = int(10 ** (digits - 1))
    upper = int(10**digits - 1)
    for x, a, b in a_generator(upper, lower):
        if is_palindrome(x):
            return (True, a, b)
    return False, upper, lower


def main():
    digits = 3
    found, a, b = find_palindrome()
    if found:
        x = a * b
        print(
            f"{a:4d} * {b:4d} = {x:8d} is a number palindrome with {digits:4d} digits"
        )
    else:
        print(
            f"no palindrome could be found for {digits:4d} digit numbers in the range from {a:8d} to {b:8d}"
        )


if __name__ == "__main__":
    main()
