import pytest
from typing import List

import utils
import pizza


@pytest.mark.parametrize(
        "pizza, topping",
        [
            (pizza.MargheritaPizza(),
             ["tomato sauce", "mozzarella", "tomatoes"]),
            (pizza.PepperoniPizza(),
             ["tomato sauce", "mozzarella", "pepperoni"]),
            (pizza.HawaiianPizza(),
             ["tomato sauce", "mozzarella", "chicken", "pineapples"])
        ]
)
def test_pizza_toppings(pizza: pizza.BasePizza, topping: List[str]):
    assert pizza.receipt() == topping


def test_invalid_pizza_size():
    invalid_size = "QWERTY"

    with pytest.raises(ValueError):
        pizza.PepperoniPizza(size=invalid_size)


def test_equal():
    first_pizza = pizza.HawaiianPizza()
    second_pizza = pizza.HawaiianPizza()

    assert first_pizza == second_pizza


def test_not_equal():
    first_pizza = pizza.PepperoniPizza()
    second_pizza = pizza.MargheritaPizza()

    assert first_pizza != second_pizza


def test_bake():
    toppings = ["sausage", "mushrooms", "cheese", "tomatoes"]
    custom_pizza = pizza.BasePizza(toppings)
    baked_pizza_time = utils.bake(custom_pizza)
    assert isinstance(baked_pizza_time, int)


def test_delivery():
    toppings = ["sausage", "mushrooms", "cheese", "tomatoes"]
    custom_pizza = pizza.BasePizza(toppings)
    delivered_pizza_time = utils.delivery(custom_pizza)
    assert isinstance(delivered_pizza_time, int)


def test_pickup():
    toppings = ["sausage", "mushrooms", "cheese", "tomatoes"]
    custom_pizza = pizza.BasePizza(toppings)
    pickup_pizza_time = utils.pickup(custom_pizza)
    assert isinstance(pickup_pizza_time, int)
