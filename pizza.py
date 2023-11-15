from typing import List, Dict


class BasePizza:
    """
    Base class for all other Pizza classes.
    Base class provides
        - __eq__ magic method to compare pizza toppings and sizes
        - __repr__ magic method that must be implemented by each child class
        - dict method to return receipt in dictionary
        - receipt classmethod to provide receipt without instantiating instance
    """
    _sizes = ["L", "XL"]
    _toppings = []

    def __init__(self, toppings: List[str], size: str = "L"):
        if size in self._sizes:
            self.size = size
        else:
            raise ValueError(f"{size} is not valid size of pizza")
        self.toppings = toppings

    def __eq__(self, other) -> bool:
        if not isinstance(other, BasePizza):
            raise TypeError(f"{other} variable is not instance of Pizza")

        return sorted(self.toppings) == sorted(other.toppings) and \
            self.size == other.size

    def __repr__(self):
        raise f"Custom Pizza: {', '.join(self.toppings)}"

    def dict(self) -> Dict[int, str]:
        toppings_dict = {i: topping for i, topping in enumerate(self.toppings)}
        return toppings_dict

    @classmethod
    def receipt(cls) -> List[str]:
        return cls._toppings


class MargheritaPizza(BasePizza):
    """
    Child class of BasePizza for Margherita
    Class has its own unique toppings that cannot be changed
    """
    _toppings = ["tomato sauce", "mozzarella", "tomatoes"]

    def __init__(self, size: str = "L"):
        super().__init__(
            toppings=self._toppings,
            size=size)

    def __repr__(self) -> str:
        return f"Margherita Pizza: {', '.join(self.toppings)}"


class PepperoniPizza(BasePizza):
    """
    Child class of BasePizza for Pepperoni
    Class has its own unique toppings that cannot be changed
    """
    _toppings = ["tomato sauce", "mozzarella", "pepperoni"]

    def __init__(self, size: str = "L"):
        super().__init__(
            toppings=self._toppings,
            size=size)

    def __repr__(self) -> str:
        return f"Pepperoni Pizza: {', '.join(self.toppings)}"


class HawaiianPizza(BasePizza):
    """
    Child class of BasePizza for Hawaiian
    Class has its own unique toppings that cannot be changed
    """
    _toppings = ["tomato sauce", "mozzarella", "chicken", "pineapples"]

    def __init__(self, size: str = "L"):
        super().__init__(
            toppings=self._toppings,
            size=size)

    def __repr__(self) -> str:
        return f"Hawaiian Pizza: {', '.join(self.toppings)}"
