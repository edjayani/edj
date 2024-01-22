from unittest import TestCase, main
from pizza import Pizzas


class TestStringMethods(TestCase):

    def test_menu(self):
        ans = ['tomato sause', 'mozzarella', 'tomatoes']
        self.assertEqual(Pizzas.classify('Margherita'), ans)

    def test_menu_wrong(self):
        ans = ['tomato sause', 'mozzarella', 'tomatoes']
        self.assertNotEqual(Pizzas.classify('Pepperoni'), ans)

    def test_size(self):
        self.assertNotEqual(Pizzas.width('L'), 30)

    def test_wrong_size(self):
        with self.assertRaises(UnboundLocalError):
            Pizzas.width('S')


if __name__ == '__main__':
    main()
