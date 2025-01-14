from django.test import TestCase
from django.urls import reverse, resolve
from users import views

class UsersUrlsTests(TestCase):
    def test_user_register_url(self):
        register_url= reverse('users:register')
        self.assertEqual(register_url, '/user/register/')

    def test_user_login_url(self):
        login_url= reverse('users:login')
        self.assertEqual(login_url, '/user/login/')


class UsersViewsTests(TestCase):
    def test_user_login_view_is_correct(self):
        user_login_view = resolve(reverse('users:login'))
        self.assertIs(user_login_view.func, views.login)

    def test_user_register_view_is_correct(self):
        user_register_view = resolve(reverse('users:register'))
        self.assertIs(user_register_view.func, views.register)