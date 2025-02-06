from django.test import TestCase
from users import views
from django.contrib.auth.models import User

#Test setups
class UsersTestBases(TestCase):
    def setUp(self) -> None:
        # User for tests
        self.user_test = self.make_user(
            first = 'userTestName',
            last = 'lastUserTestName',
            username = 'user.test.name',
            password = '12345679',
            email = 'testUser@email.com'
        )

        return super().setUp()

    #Function to create categories
    def make_user(self,
            first = 'firstName',
            last = 'lastName',
            username = 'username.test',
            password = '123456',
            email = 'test@email.com'
            ):
        return User.objects.create_user(
            first_name = first,
            last_name = last,
            username = username,
            password = password,
            email = email,
        )

