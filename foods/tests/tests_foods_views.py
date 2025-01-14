from django.test import TestCase
from django.urls import reverse, resolve
from foods import views

class FoodsViewsTests (TestCase):
    def test_food_main_view_is_correct(self):
        view_main = resolve(reverse('foods:main'))
        self.assertIs(view_main.func, views.main)

    def test_show_food_view_is_correct(self):
        show_food_view = resolve(reverse('foods:show_food'))
        self.assertIs(show_food_view.func, views.show_food)

    def test_add_food_view_is_correct(self):
        add_food_view = resolve(reverse('foods:add_food'))
        self.assertIs(add_food_view.func, views.add_food)
