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

#Tests for Login user view
class LoginUsersViewsTests(UsersTestBases):

     #Test if the user login view is returning correct
    def test_user_login_view_is_correct(self):
        user_login_view = resolve(reverse('users:login'))
        self.assertIs(user_login_view.func, views.login)