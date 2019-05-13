'''Test the views of authentication app.'''
from django.test import TestCase
# rest framework
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from userapp.models import User


from authenticationapp.views import JSONWebTokenObtain


# token-auth',JSONWebTokenObtain.as_view()),
#     path('token-auth-refresh',JSONWebTokenRefresh.as_view()),
#     path('token-auth-verify'
class AuthViewsTest(APITestCase):
    # stress = mommy.make(MaximumAllowableStress)
    def setUp(self):
        """
        Set up all the tests
        """
        self.url = reverse('token-auth')
        self.username = 'john'
        self.email = 'johnking@got.com'
        self.password = 'popularchoice'
        self.first_name = 'John'
        self.last_name = 'Snow'
        self.user = User.objects.create_superuser(
            self.username, self.email, self.password, self.first_name, self.last_name)

    def test_auth_without_pass(self):
        data = {
            'username': self.username,
        }
        response = self.client.post(self.url, data)
        response_json = json.loads(response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response_json)
        self.assertTrue('password' in response_json['errors'])

    def test_auth_with_wrong_pass(self):
        data = {
            'username': self.username,
            'password': 'wrong-password'
        }
        response = self.client.post(self.url, data)
        response_json = json.loads(response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response_json)
        self.assertTrue('error' in response_json['errors'])

    def test_auth_with_no_user(self):
        data = {}
        response = self.client.post(self.url, data)
        response_json = json.loads(response.content)
        self.assertEqual(400, response.status_code)
        self.assertTrue('errors' in response_json)
        self.assertTrue('username' in response_json['errors'])

    def test_auth_with_valid_data(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(self.url, data)
        response_json = json.loads(response.content)
        self.assertEqual(200, response.status_code)
        self.assertTrue('data' in response_json)
        self.assertTrue('token' in response_json['data'])