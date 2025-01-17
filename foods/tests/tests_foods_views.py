from django.test import TestCase
from django.urls import reverse, resolve
from foods import views

class FoodsViewsTests (TestCase):
    def test_food_main_view_is_correct(self):
        view_main = resolve(reverse('foods:home'))
        self.assertIs(view_main.func, views.home)

    def test_show_food_view_is_correct(self):
        show_food_view = resolve(reverse('foods:show_food'))
        self.assertIs(show_food_view.func, views.show_food)

    def test_add_food_view_is_correct(self):
        add_food_view = resolve(reverse('foods:add_food'))
        self.assertIs(add_food_view.func, views.add_food)
    
    def test_home_food_view_returns_200_ok(self):
        response = self.client.get(reverse('foods:home'))
        self.assertEqual(response.status_code, 200)

    def test_show_food_view_returns_200_ok(self):
        response = self.client.get(reverse('foods:show_food'))
        self.assertEqual(response.status_code, 200)

    def test_add_food_view_returns_200_ok(self):
        self.client.login(username='caue', password='teste12345')

        response = self.client.get(reverse('foods:add_food'))
        self.assertEqual(response.status_code, 200)