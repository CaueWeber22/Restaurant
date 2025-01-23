from django.test import TestCase
from django.urls import reverse, resolve
from foods import views
from .tests_foods_base import FoodsTestBases

class FoodsViewsTests (FoodsTestBases):
    #Test for visualization in home is correct
    def test_food_main_view_is_correct(self):
        view_main = resolve(reverse('foods:home'))
        self.assertIs(view_main.func, views.home)
    
    #Test for visualization in show_food is correct
    def test_show_food_view_is_correct(self):
        show_food_view = resolve(reverse('foods:show_food'))
        self.assertIs(show_food_view.func, views.show_food)

    #Test for visualization in add_food is correct  
    def test_add_food_view_is_correct(self):
        add_food_view = resolve(reverse('foods:add_food'))
        self.assertIs(add_food_view.func, views.add_food)
    
    #Test if the home view returns status 200
    def test_home_food_view_returns_200_ok(self):
        response = self.client.get(reverse('foods:home'))
        self.assertEqual(response.status_code, 200)

    #Test if the show_food view returns status 200
    def test_show_food_view_returns_200_ok(self):
        response = self.client.get(reverse('foods:show_food'))
        self.assertEqual(response.status_code, 200)

    #Test if the add_food view returns status 200
    def test_add_food_view_returns_200_ok(self):
        login = self.client.login(username='teste', password='test12345')
        self.assertTrue(login, "Login Failed")

        response = self.client.get(reverse('foods:add_food'))
        self.assertEqual(response.status_code, 200)

    # test if show_food filter for available foods is correct
    def test_show_food_load_available_foods(self):
        self.make_food(is_available = True)

        response = self.client.get(reverse('foods:show_food'))

        self.assertEqual(response.status_code, 200)
