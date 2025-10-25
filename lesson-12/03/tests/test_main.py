import pytest
from main import multiply

#############################
# Testcases
#############################
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_multiply_with_string():
    with pytest.raises(TypeError, match='Both arguments must be integers'):
        multiply(2, '3')
