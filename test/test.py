import pytest
from src import two_digit_numbers
from src import base26
from src import palindrome


# pytest.mark.parametrize("values, result", (["32", "5", "754", "-5", "-50", "99", "0"], ["5", "754", "-5", "0"]))
def test_two_digit_removal():
    assert two_digit_numbers.two_digit_numbers(["32", "5", "754", "-5", "-50", "99", "0"]) == ["5", "754", "-5", "0"]

def test_base26():
    assert base26.base26(28) == "ab"
    assert base26.unbase26("ab") == 28

def test_palindrome():
    assert palindrome.palindrome2("hannah") == True
    assert palindrome.palindrome2("bussin fr no cap") == False