# contents of test_append.py
import pytest

# eg2:fixtures​​如何使用其他​​fixtures  demo
@pytest.fixture
def first_entry():
    return "a"


# order本身作为一个fixture，请求了另一个fixture即first_entry
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    # [a].append("b") --> ["a","b"]
    order.append("b")  

    # Assert
    assert order == ["a", "b"]