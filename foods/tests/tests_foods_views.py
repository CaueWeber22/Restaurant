from django.test import TestCase
from django.urls import reverse, resolve
from foods import views
from .tests_foods_base import FoodsTestBases
from foods.models import Food, Category

#Test for main views
class FoodsHomeViewTests (FoodsTestBases):
    #Test for visualization in home is correct
    def test_food_home_view_is_correct(self):
        view_main = resolve(reverse('foods:home'))
        self.assertIs(view_main.func, views.home)

    #Test if the home view returns status 200
    def test_home_food_view_returns_200_ok(self):
        response = self.client.get(reverse('foods:home'))
        self.assertEqual(response.status_code, 200)


#Test for add foods view
class FoodsAddFoodViewTests (FoodsTestBases):

    #Test for visualization in add_food is correct  
    def test_add_food_view_is_correct(self):
        add_food_view = resolve(reverse('foods:add_food'))
        self.assertIs(add_food_view.func, views.add_food)

    #Test if the add_food view returns status 200
    def test_add_food_view_returns_200_ok(self):
        login = self.client.login(username='teste', password='test12345')
        self.assertTrue(login, "Login Failed")

        response = self.client.get(reverse('foods:add_food'))
        self.assertEqual(response.status_code, 200)

    #Test the post add_food
    def test_add_food_function_create_new_food(self):
        login = self.client.login(username='teste', password='test12345')
        self.assertTrue(login, "Login Failed")

        response = self.client.post(reverse('foods:add_food'), data={
            'name': 'creationTeste',
            'price': self.food_test.price,
            'category_id': self.category_test.id,
            'description': self.food_test.description,
            'image': 'test'
            })
        
        self.assertTrue(Food.objects.filter(name='creationTeste').exists())
        
        self.assertEqual(response.status_code, 302)


#Test for show foods view
class FoodsShowFoodViewTests (FoodsTestBases):

    #Test for visualization in show_food is correct
    def test_show_food_view_is_correct(self):
        show_food_view = resolve(reverse('foods:show_food'))
        self.assertIs(show_food_view.func, views.show_food)

    #Test if the show_food view returns status 200
    def test_show_food_view_returns_200_ok(self):
        response = self.client.get(reverse('foods:show_food'))
        self.assertEqual(response.status_code, 200)

    # test if show_food filter for available foods is correct
    def test_show_food_load_available_foods(self):
        self.make_food(is_available = True)

        response = self.client.get(reverse('foods:show_food'))

        self.assertEqual(response.status_code, 200)


#Test for show foods view
class FoodsSearchFoodViewTests (FoodsTestBases):

    def setUp(self):
        self.category1 = Category.objects.create(category_type="CategoryOne")
        self.category2 = Category.objects.create(category_type="CategoryTwo")

        self.food1 = Food.objects.create(name="FoodOne", price=50, category=self.category1, is_available=True)
        self.food2 = Food.objects.create(name="FoodTwo", price=50, category=self.category2, is_available=True)
        self.food3 = Food.objects.create(name="FoodThree", price=50, category=self.category2, is_available=True)


    #Test for search food view is correct
    def test_show_food_search_view_is_correct(self):
        search_food = resolve(reverse('foods:food_search'))
        self.assertIs(search_food.func, views.food_search)

    #Test if the search without filter redirect to 'show_food'
    def test_search_without_filters_redirects(self):
        response = self.client.get(reverse('foods:food_search'))
        self.assertEqual(response.status_code, 302)  

    def test_search_by_category(self):
        response = self.client.get(reverse('foods:food_search'), {'category': self.category1.id})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'FoodOne')      
        self.assertNotContains(response, 'FoodTwo')   

    def test_search_by_name(self):
        response = self.client.get(reverse('foods:food_search'), {'name': self.food1.name})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'FoodOne')      
        self.assertNotContains(response, 'FoodTwo')   

    def test_search_by_name_and_category(self):
        response = self.client.get(reverse('foods:food_search'), {'category': self.category1.id, 'name': self.food1.name})  

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'FoodOne')
        self.assertNotContains(response, 'FoodTwo')

#Test for delete view
class FoodsDeleteViewTests (FoodsTestBases):

    #Test for visualization in delete_food is correct  
    def test_delete_view_is_correct(self):
        delete_food_view = resolve(reverse('foods:delete_food', kwargs={'food_id': self.food_test.id}))
        self.assertIs(delete_food_view.func, views.delete_food)

    #Test if the delete view returns status 200
    def test_delete_view_returns_204_ok(self):
        login = self.client.login(username='teste', password='test12345')
        self.assertTrue(login, "Login Failed")

        self.food_del = self.make_food()
        
        food_id = self.food_del.id
        self.client.post(reverse('foods:delete_food', kwargs={'food_id':food_id}))

        # Verifica se a comida foi deletada
        with self.assertRaises(Food.DoesNotExist):
            Food.objects.get(id=food_id)