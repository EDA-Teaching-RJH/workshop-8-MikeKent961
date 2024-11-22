from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

def testCalc():
    assert add(2, 4) == 6
    assert add(9, -3) == 6
    assert subtract(2, 4) == -2
    assert subtract(9, -3) == 12
    assert multiply(2, 4) == 8
    assert multiply(9, -3) == -27
    assert divide(2, 4) == 0.5
    assert divide(9, -3) == -3

    try:
        assert divide(10, 0) == True
    except ZeroDivisionError:
        print("")