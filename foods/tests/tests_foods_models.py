from foods.models import Food
from .tests_foods_base import FoodsTestBases
from django.core.exceptions import ValidationError
from parameterized import parameterized, parameterized_class



class FoodsModelsTests (FoodsTestBases):
   #Set up for tests
   def setUp(self):
      self.food = self.make_food()

      return super().setUp()

   #Test if an error occurs when trying to create food name and description that exceed the character limit.
   @parameterized.expand([
         ('name', 50),
         ('description', 50),
      ])
   def test_fields_max_length(self, field, max_length):
      setattr(self.food, field, 'A' * (max_length + 1))
      with self.assertRaises(ValidationError):
         self.food.full_clean()

   #Test food price max length
   def test_food_price_max_value_length(self):
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
   
   #Test the food str representation
   def test_food_string_representations(self):
      self.food.name = 'Testing'
      self.food.full_clean()
      self.assertEqual(str(self.food), 'Testing')
   
   #Test the category str representation
   def test_category_string_representations(self):
      self.category_test.category_type = 'Testing'
      self.food.full_clean()
      self.assertEqual(str(self.category_test), 'Testing')
