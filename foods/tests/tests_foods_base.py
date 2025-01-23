from django.test import TestCase
from django.urls import reverse, resolve
from foods import views
from foods.models import Food, Category 
from django.contrib.auth.models import User

#Test setups
class FoodsTestBases(TestCase):
    def setUp(self) -> None:
        # Category for tests
        self.category_test = self.make_category()

        # Food for tests
        self.food_test = self.make_food()
        
        #User for tests
        self.user = User.objects.create_user(username='teste', password='test12345')

        return super().setUp()

    #Function to create categories
    def make_category(self, category = "Test_catego"):
        return Category.objects.create(category_type=category)

    #Function to create foods    
    def make_food(self, 
                name='food_test',
                price=50,
                description='food...',
                is_available=True 
            ):
        return Food.objects.create(
            name = name,
            price = price,
            description = description,
            is_available = is_available,  
            category = self.make_category()
        )