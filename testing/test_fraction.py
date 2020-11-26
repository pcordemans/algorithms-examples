from fraction import Fraction

def test_equality():
    one_half = Fraction(1,2)
    another_half = Fraction(1,2)
    assert one_half == another_half

def test_str():
    one_half = Fraction(1, 2)
    assert str(one_half) == "1\n-\n2"

def test_equality_normalized():
    one_half = Fraction(1,2)
    two_fourths = Fraction(2,4)
    assert one_half == two_fourths