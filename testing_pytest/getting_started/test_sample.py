import pytest


def func(x):
    return x + 1


def test_func():
    assert func(3) == 5


def even_func():
    """For some reason, this function does not behave properly"""
    return 3


def test_even():
    assert even_func() % 2 == 0, "value was odd, should be even"


def recursion_func():
    recursion_func()


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        recursion_func()
    assert "maximum recursion" in str(excinfo.value)


def my_func_raises_value_error():
    raise ValueError("Something 123 something")


def test_my_func_raises_value_error():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        my_func_raises_value_error()


def test_my_func_raises_value_error_1():
    pytest.raises(ValueError, my_func_raises_value_error)
