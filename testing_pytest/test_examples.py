import pytest


# NOTES: BASICS

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

# NOTES: FIXTURES

## Quick example

@pytest.fixture
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")


class TestOne:
    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert ["one", "outer"] == order


class TestTwo:
    @pytest.fixture
    def inner(self, order):
        order.append("two")

    def test_order(self, order, outer):
        assert ["two", "outer"] == order


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self, ):
        for fruit in self.fruit:
            fruit.cube()


@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(*fruit_bowl)
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


## Fixtures request other fixtures

@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order_one(first_entry):
    return [first_entry]


def test_string_one(order_one):
    order_one.append("b")
    assert ["a", "b"] == order_one


## Fixtures are reusable: `order_one` is reused

def test_int_one(order_one):
    order_one.append(2)
    assert ["a", 2] == order_one


## A test/fixture can request more than one fixture at a time
@pytest.fixture
def second_entry():
    return 2


@pytest.fixture
def order_two(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string_one(order_two, expected_list):
    order_two.append(3.0)
    assert order_two == expected_list


## Fixtures being requested more than once per test, then the return values are
## cached
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    """
    When append_first is executed, order is updated and cached.
    """
    assert order == [first_entry]


## Autouse fixtures
@pytest.fixture
def order_updated():
    return []


@pytest.fixture(autouse=True)
def append_first_autouse(order_updated, first_entry):
    return order_updated.append(first_entry)


def test_string_only_one(order_updated, first_entry):
    """
    We dont have to pass the append_first_autouse fixture into the test
    function as in the test_string_only case.
    """
    assert order_updated == [first_entry]


def test_string_and_int_one(order_updated, first_entry):
    order_updated.append(2)
    assert order_updated == [first_entry, 2]
