import pytest

from FizzBuzzTDD.main import fizzBuzz


def checkFizzBuzz(value, expected_value):
    result = fizzBuzz(value)
    assert result == expected_value

def test_canCallFizzBuzz():
    fizzBuzz(1)


def test_fizzBuzzReturnFizzWhen3IsPassedIn():
    checkFizzBuzz(3, 'fizz')


def test_fizzBuzzReturnNon0When2IsPassedIn():
    checkFizzBuzz(2, 'No no')


def test_fizzBuzzReturnBuzzWhen5IsPassedIn():
    checkFizzBuzz(5, 'buzz')


def test_fizzBuzzReturnNonoWhen2IsPassedIn():
    checkFizzBuzz(2, 'No no')


def test_fizzBuzzReturnFizzBuzzWhen15IsPassedIn():
    checkFizzBuzz(15, 'fizz buzz')

