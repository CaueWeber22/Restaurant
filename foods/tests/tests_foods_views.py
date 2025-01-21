from django.test import TestCase
from django.urls import reverse, resolve
from foods import views
from foods.models import Food, Category 
from django.contrib.auth.models import User

#Test setups
class FoodsTestBases(TestCase):
    def setUp(self) -> None:
         # Category for tests
        self.category_test = Category.objects.create(category_type="Category_test")

        # Food for tests
        self.food_test = Food.objects.create(
            name='food_test',
            price=50,
            description='A food for tests',
            is_available=True,  
            category=self.category_test 
        )
       
        #User for tests
        self.user = User.objects.create_user(username='teste', password='test12345')

        return super().setUp()

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

