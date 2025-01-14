from django.test import TestCase
from django.urls import reverse

class UsersUrlsTests(TestCase):
    def test_user_register_url(self):
        register_url= reverse('users:register')
        self.assertEqual(register_url, '/user/register/')

    def test_user_login_url(self):
        login_url= reverse('users:login')
        self.assertEqual(login_url, '/user/login/')

