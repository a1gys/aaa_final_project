from typing import Callable, Optional
from random import randint

import pizza as pizza_lib


def log(msg: Optional[str] = None) -> Callable:
    """
    Decorator function that print the name of function and time spend
    Custom message can be used to replace default print
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, pizza_lib.BasePizza):
                    raise TypeError(f"{arg} is not in the menu")

            time = func(*args)
            name = func.__name__
            if msg:
                try:
                    print(msg.format(time))
                except BaseException:
                    print(msg)
            else:
                print(f"{name} - {time} seconds!")
            return time
        return wrapper
    return decorator


@log()
def bake(pizza: pizza_lib.BasePizza) -> int:
    """
    Bakes the pizza
    """
    time = randint(1, 10)
    return time


@log("🛵Delivered in {} seconds!")
def delivery(pizza: pizza_lib.BasePizza) -> int:
    """
    Delivers the pizza
    """
    time = randint(1, 10)
    return time


@log("🏡Picked up in {} seconds!")
def pickup(pizza: pizza_lib.BasePizza) -> int:
    """
    Pickup the order
    """
    time = randint(1, 10)
    return time
