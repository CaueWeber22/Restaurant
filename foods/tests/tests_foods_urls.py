from django.test import TestCase
from django.urls import reverse

class FoodsUrlsTests(TestCase):
    def test_food_main_url(self):
        home_url= reverse('foods:home')
        self.assertEqual(home_url, '/')

    def test_show_food_url(self):
        show_food_url= reverse('foods:show_food')
        self.assertEqual(show_food_url, '/show/')

    def test_add_food_url(self):
        add_food_url= reverse('foods:add_food')
        self.assertEqual(add_food_url, '/add/')

    def test_food_search_url_is_correct(self):
        url = reverse('foods:food_search')
        self.assertEqual(url, '/show/search/')