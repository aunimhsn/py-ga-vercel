from utils.calc import addition, substraction


def test_addition():
    assert addition(5, 5) == 10

def test_substraction():
    assert substraction(5, 5) == 0