import pytest

def check_age(age):
    if age < 0:
        return 'Error -'
    elif age < 13:
        return 'Child'
    elif age < 18:
        return 'Teen'
    elif age < 135:
        return 'Adult'
    else:
        return 'Error +'

# def test_math():
#     assert 2 + 2 == 4
#     assert 3 + 3 == 6
#     assert 4 * 4 == 16
#
#
# def test_logic():
#     assert (5 > 2) == True
#     assert (5 == 5) == True

def test_positive():
    assert check_age(-1) == 'Error -'
    assert check_age(10) == 'Child'
    assert check_age(15) == 'Teen'
    assert check_age(22) == 'Adult'
    assert check_age(140) == 'Error +'

def test_range():
    assert check_age(-1) == 'Error -'
    assert check_age(0) == 'Child'
    assert check_age(1) == 'Child'
    assert check_age(12) == 'Child'
    assert check_age(13) == 'Teen'
    assert check_age(14) == 'Teen'
    assert check_age(17) == 'Teen'
    assert check_age(18) == 'Adult'
    assert check_age(19) == 'Adult'
    assert check_age(134) == 'Adult'
    assert check_age(135) == 'Error +'
    assert check_age(136) == 'Error +'