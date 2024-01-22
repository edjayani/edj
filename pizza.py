import click
import functools
import random


def log(text=str, text2=str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            p = random.randint(1, 42)
            result = func(*args, **kwargs)
            print(f" {text}{p}{text2}")

        return wrapper

    return decorator


@click.group()
def cli():
    pass


class Pizzas:

    def __init__(self, name: str, size: str):
        self.name = name,
        self.size = size,
        self.ingredients = []

    def classify(name):
        """Определяет состав по названию"""
        if name == 'Margherita':
            ingredients = ['tomato sause', 'mozzarella', 'tomatoes']
        elif name == 'Pepperoni':
            ingredients = ['tomato sause', 'mozzarella', 'pepperoni']
        else:
            ingredients = ['tomato sause', 'mozzarella', 'chicken', 'pineapples']
        return ingredients

    @staticmethod
    def width(size="L"):
        """Определяет ширину пиццы"""
        if size == 'L':
            width1 = 35
        elif size == 'XL':
            width1 = 40
        return width1


@log('🍳Приготовили за ', 'с!')
def bake(name: str, size='L'):
    """ Cooks your pizza"""


@log('🛴Доставили за ', 'с!')
def deliver(name):
    """Delivers your pizza"""


@log('🏠Подождали Вас всего ', 'с!')
def pickup(name):
    """Pickups your pizza"""


@cli.command()
@click.argument("meal", nargs=1)
@click.argument("size", default="L")
@click.option("--delivery", default=False, is_flag=True)
def order(meal: str, size: str, delivery: bool):
    """Обрабатывает Ваш заказ"""
    bake(meal, size)
    if delivery:
        deliver(meal)
    pickup(meal)


@cli.command()
def menu():
    """Показывает блюда и их состав"""
    positions = {'Margherita🧀': Pizzas.classify('Margherita🧀'),
                 'Pepperoni🍕': Pizzas.classify('Pepperoni🍕'),
                 'Hawaiian🍍': Pizzas.classify('Hawaiian🍍')}
    for key in positions:
        print(str(key), end=': ')
        consist = ''
        for ingr in positions[key]:
            consist = consist + str(ingr) + ', '
        print(consist[:len(consist) - 2])


if __name__ == "__main__":
    cli()
