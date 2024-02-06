import pytest

from credit_check import credit_check

def test_valid_string_input_one():
    assert credit_check('5541808923795240') == "The number is valid!"

def test_valid_string_input_two():
    assert credit_check("4024007136512380") == "The number is valid!"

def test_valid_string_input_three():
    assert credit_check("6011797668867828") == "The number is valid!"

def test_invalid_string_input_one():
    assert credit_check("5541801923795240") == "The number is invalid!"

def test_invalid_string_input_two():
    assert credit_check("4024007106512380") == "The number is invalid!"
    
def test_invalid_string_input_three():
    assert credit_check("6011797668868728") == "The number is invalid!"

def test_valid_num_input():
    assert credit_check(6011797668867828) == "The number is valid!"

def test_invalid_num_input():
    assert credit_check(5541801923795240) == "The number is invalid!"

def test_too_few_numbers():
    assert credit_check(6011867828) == "The number is invalid!"

def test_too_many_numbers():
    assert credit_check(554180192354354795240) == "The number is invalid!"