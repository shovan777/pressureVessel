import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from userapp.models import User

from userapp.views import RegistrationNormalUserAPIView,RegistrationSuperUserAPIView,UserRetrieveUpdateAPIView

class UserViewsTest(APITestCase):

    def setUp(self):
        self.url1 = reverse('usercreate')
        self.url2 = reverse('userupdate')
        self.url3 = reverse('superusercreate')
        self.username = "john"
        self.email = "johnking@got.com"
        self.password = 'popularchoice'
        self.first_name = 'John'
        self.last_name = 'Snow'
        
    def test_user_without_data(self):
        data = {
            'user': {

            }
        }
        response = self.client.post(self.url1, data, format='json')
        response_json = json.loads(response.content)
        self.assertEqual(400,response.status_code)
        self.assertTrue('errors' in response_json)
        self.assertTrue('error' in response_json['errors'])

    def test_user_with_data(self):
        data = {
            'user':{
                'username': self.username,
                'email': self.email,
                'password' : self.password,
                'first_name':self.first_name,
                'last_name':self.last_name
            }
        }
        response = self.client.post(self.url1, data, format='json')
        response_json = json.loads(response.content)
        self.assertEqual(200,response.status_code)
        print(response_json)
        self.assertTrue('success' in response_json)