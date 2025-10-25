import pytest
from main import Division
from main import Multiplication

#############################
# Fixtures
#############################
@pytest.fixture(scope='function')
def multiplication():
    return Multiplication()

@pytest.fixture(scope='function')
def division():
    return Division()

#############################
# Testcases
#############################
def test_multiplication(multiplication):
    assert multiplication.calculate(3, 4) == 12
    assert multiplication.calculate(-2, 5) == -10
    assert multiplication.calculate(0, 100) == 0
    assert multiplication.calculate(2.5, 4) == 10.0

def test_division(division):
    assert division.calculate(8, 2) == 4
    assert division.calculate(-9, 3) == -3
    assert division.calculate(7.5, 2.5) == 3.0
