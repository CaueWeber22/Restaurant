from django.test import TestCase
from django.urls import reverse

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