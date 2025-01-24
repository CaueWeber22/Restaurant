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

   #Test food price max length
   def test_food_price_max_length(self):
      self.food.price = 12345678901234
      
      with self.assertRaises(ValidationError):
         self.food.full_clean()

   #Test food price max decimal places
   def test_food_price_max_decimal_places(self):
      self.food.price = 123.2324
      
      with self.assertRaises(ValidationError):
         self.food.full_clean()      

   #Test category category_type max length 
   def test_category_category_type_max_length(self):
      self.category_test.category_type = 'a' * 60
      
      with self.assertRaises(ValidationError):
         self.category_test.full_clean()      

   #Test if foods are set by default to true at creation
   def test_food_is_available_is_default_true(self):
      food = Food.objects.create(
            name = 'food',
            price = 50,
            description = 'a',
            category = self.make_category()
        )
      
      self.assertEqual(food.is_available, True)

   #Test foods images are set by default to "no_image"
   def test_food_image_is_default_text_is_ok(self):
      food = self.make_food()
      
      self.assertEqual(food.image, "no_image")

   #Test if food name cant be null
   def test_if_food_name_cant_be_null(self):
      self.food.name = None
      
      with self.assertRaises(ValidationError):
         self.food.full_clean()  
  
   #Test food price cant be null
   def test_if_food_price_cant_be_null(self):
      self.food.price = None
      
      with self.assertRaises(ValidationError):
         self.food.full_clean()

   #Test food category cant be null
   def test_if_food_category_cant_be_null(self):
      self.food.category = None
      
      with self.assertRaises(ValidationError):
         self.food.full_clean()        

   #Test if category category_type can be null
   def test_if_category_category_type_cant_be_null(self):
      self.category_test.category_type = None
      
      with self.assertRaises(ValidationError):
         self.category_test.full_clean()    

