import pytest
from fizzbuzz import fizzbuzz

def test_fizz():
    assert fizzbuzz(4) == ['1', '2', 'Fizz']

def test_buzz():
    assert fizzbuzz(6) == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizzbuzz():
    assert fizzbuzz(16) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    assert fizzbuzz(31) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz']

test_fizzbuzz()
