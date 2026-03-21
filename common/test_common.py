"""
tests for common.py of project euler
"""
from .common import first_primes, is_prime

import pytest

@pytest.mark.parametrize( "actual,expected", [(7, True), (11, True), (1000, False)])
def test_is_prime(actual, expected):
    if expected:
        assert is_prime(actual), f"{actual} should be prime but came back as not"
        return

    assert not is_prime(actual), f"{actual} is not prime but came back as such"

def test_module():
    for p in first_primes:
        assert is_prime(p), f"{p} is in first_primes but came back as not prime"