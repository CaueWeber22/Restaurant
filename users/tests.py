from django.test import TestCase
from django.urls import reverse

class FoodsUrlsTests(TestCase):
    def test_user_register_url(self):
        register_url= reverse('users:register')
        self.assertEqual(register_url, 'register/')



    
