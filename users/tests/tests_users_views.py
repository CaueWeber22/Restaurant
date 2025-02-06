from django.urls import reverse, resolve
from users import views
from .tests_user_bases import UsersTestBases
from django.contrib.auth.models import User

#Tests for Register user view
class RegisterUsersViewsTests(UsersTestBases):

    #Test if the user register view is returning correct
    def test_user_register_view_is_correct(self):
        user_register_view = resolve(reverse('users:register'))
        self.assertIs(user_register_view.func, views.register)

    #Test the get method status in the user register function
    def test_user_register_get_is_returning_200(self):
        response = self.client.get(reverse('users:register'))
        
        self.assertEqual(response.status_code, 200)

    #Test the get method in the user register function
    def test_user_register_post_is_ok(self):
        response = self.client.post(reverse('users:register'), data={
            'firstname': self.user_test.first_name,
            'lastname': self.user_test.last_name,
            'username': 'user_for_test_post',
            'password': self.user_test.password,
            'email': self.user_test.email,
        })
        
        self.assertTrue(User.objects.filter(username='user_for_test_post').exists())

        self.assertEqual(response.status_code, 302)

    #Test the status returned if exists an user with the same username
    def test_user_register_post_status_with_repeated_name(self):
        response = self.client.post(reverse('users:register'), data={
            'firstname': self.user_test.first_name,
            'lastname': self.user_test.last_name,
            'username': self.user_test.username, #Same name of the user created in setup
            'password': self.user_test.password,
            'email': self.user_test.email,
        })

        self.assertEqual(response.status_code, 409)

#Tests for Login user view
class LoginUsersViewsTests(UsersTestBases):

     #Test if the user login view is returning correct
    def test_user_login_view_is_correct(self):
        user_login_view = resolve(reverse('users:login'))
        self.assertIs(user_login_view.func, views.login)
        
    #Test the get method status in the user login view
    def test_user_login_get_is_returning_200(self):
        response = self.client.get(reverse('users:login'))
        
        self.assertEqual(response.status_code, 200)

   
   #Test if the login auth returns status 200 when the user validate is correct
    def test_login_auth_function_returns_200(self):
        
        response = self.client.post(reverse('users:login'), data={
            'username': self.user_test.username,
            'password': '12345679' #Mocked password at the user_test creation
        })

        self.assertEqual(response.status_code, 200)

    #Test if the login auth returns status 404 if the user doesnt exist
    def test_login_auth_function(self):
        
        response = self.client.post(reverse('users:login'), data={
            'username': 'non-existent',
            'password': 'non-existent' 
        })

        self.assertEqual(response.status_code, 404)