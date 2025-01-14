from django.test import TestCase
from django.urls import reverse, resolve
from foods import views

class FoodsUrlsTests(TestCase):
    def test_food_main_url(self):
        main_url= reverse('foods:main')
        self.assertEqual(main_url, '/')

    def test_show_food_url(self):
        show_food_url= reverse('foods:show_food')
        self.assertEqual(show_food_url, '/show/')

    def test_add_food_url(self):
        add_food_url= reverse('foods:add_food')
        self.assertEqual(add_food_url, '/add/')


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
