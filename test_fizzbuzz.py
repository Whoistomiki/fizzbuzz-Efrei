import pytest
from io import StringIO
from unittest.mock import patch
from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    with patch('sys.stdout', new_callable=StringIO) as fizzbuzz_test:
        fizzbuzz()

        output = fizzbuzz_test.getvalue()

        expected_output = ""
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                expected_output += "FizzBuzz\n"
            elif i % 3 == 0:
                expected_output += "Fizz\n"
            elif i % 5 == 0:
                expected_output += "Buzz\n"
            else:
                expected_output += f"{i}\n"

        assert output == expected_output
