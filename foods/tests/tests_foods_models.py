from django.test import TestCase
from django.urls import reverse, resolve
from foods import views
from foods.models import Food
from .tests_foods_base import FoodsTestBases
from django.core.exceptions import ValidationError



class FoodsModelsTests (FoodsTestBases):
   #Set up for tests
   def setUp(self):
      self.food = self.make_food()

      return super().setUp()

   #Test if an error occurs when trying to create food name with more than 50 chars
   def test_food_name_raise_error_if_name_has_more_than_50_char(self):
      self.food.name = 'A'*65

      with self.assertRaises(ValidationError):
        self.food.full_clean()

   #Test if an error occurs when trying to create food name with more than 50 chars
   def test_food_description_raise_error_if_has_more_than_50_char(self):
      self.food.description = 'A'*65

      with self.assertRaises(ValidationError):
        self.food.full_clean()        

   #Test if foods are set by default to true at creation
   def test_food_is_available_is_default_true(self):
      food = Food.objects.create(
            name = 'food',
            price = 50,
            description = 'a',
            category = self.make_category()
        )
      
      self.assertEqual(food.is_available, True)




