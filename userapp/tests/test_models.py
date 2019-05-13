from django.test import TestCase
from model_mommy import mommy

from userapp.models import User,UserMangaer

class UserModelsTest(TestCase):

    def test_UserString(self):
        user = mommy.make(User)
        self.assertTrue(isinstance(user, User))
        self.assertTrue(isinstance(user.__str__(),str))
        self.assertEqual(user.__str__(), user.username)

class UserMangaerTest(TestCase):

    def test_CreateUser(self):
        expected_val = "john"
        user1 = User.objects.create_user(
            username="john",
            email="johnking@got.com",
            password="popularchoice",
            first_name="John",
            last_name="Snow")
        ret_val = user1.username
        self.assertTrue(isinstance(user1,User))
        self.assertEqual(expected_val,ret_val)
        self.assertEqual(False,user1.is_active)

    def test_CreateSuperUser(self):
        expected_val = "john"
        user1 = User.objects.create_superuser(
            username="john",
            email="johnking@got.com",
            password="popularchoice",
            first_name="John",
            last_name="Snow")
        ret_val = user1.username
        self.assertTrue(isinstance(user1,User))
        self.assertEqual(expected_val,ret_val)
        self.assertEqual(True,user1.is_active)
        self.assertEqual(True,user1.is_superuser)
        self.assertEqual(True,user1.is_staff)