from quiz import add_numbers, multiply_numbers

def test_add():
    assert add_numbers(5, 10) == 15

def test_multiply():
    assert multiply_numbers(5, 10) == 50

def test_result():
    result = add_numbers(5, 10) * 2
    assert result == 30
