from random import randint
from typing import Optional
import click

from pizza import MargheritaPizza, PepperoniPizza, HawaiianPizza
import utils


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """
    Menu of the Pizzeria
    """
    print(f"- Margherita 🧀: {', '.join(MargheritaPizza.receipt())}")
    print(f"- Pepperoni 🍕: {', '.join(PepperoniPizza.receipt())}")
    print(f"- Hawaiian 🍍: {', '.join(HawaiianPizza.receipt())}")


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool, size: Optional[str] = None):
    """
    Prepares the ordered pizza
    If delivery is true, then also delivers the order
    """

    if not size:
        size = "L"
    if pizza == "pepperoni":
        food = PepperoniPizza(size=size)
    elif pizza == "margherita":
        food = MargheritaPizza(size=size)
    elif pizza == "hawaiian":
        food = HawaiianPizza(size=size)
    else:
        raise ValueError(f"{food.title()} is not in the menu.")

    cooked_time = randint(1, 10)
    print(f"👨‍🍳 The order took {cooked_time} seconds!")
    if delivery:
        utils.delivery(food)
    else:
        utils.pickup(food)


if __name__ == "__main__":
    cli()
