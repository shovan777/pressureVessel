import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from userapp.models import User

from userapp.views import RegistrationNormalUserAPIView,RegistrationSuperUserAPIView

class NormalUserViewsTest(APITestCase):

    def setUp(self):
        self.url = reverse('usercreate')
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
        response = self.client.post(self.url, data, format='json')
        response_json = json.loads(response.content)
        self.assertEqual(400, response.status_code)
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
        response = self.client.post(self.url, data, format='json')
        response_json = json.loads(response.content)
        self.assertEqual(201,response.status_code)
        self.assertTrue('success' in response_json)

class SuperUserViewsTest(APITestCase):

    def setUp(self):
        self.url = reverse('superusercreate')
        self.username = "john"
        self.email = "johnking@got.com"
        self.password = 'popularchoice'
        self.first_name = 'John'
        self.last_name = 'Snow'

    def test_user_super_user_without_data(self):
        data = {
            'user': {

            }
        }
        response = self.client.post(self.url, data, format='json')
        response_json = json.loads(response.content)
        self.assertEqual(400,response.status_code)
        self.assertTrue('errors' in response_json)
        self.assertTrue('error' in response_json['errors'])

    def test_super_user_with_data(self):
        data = {
            'user':{
                'username': self.username,
                'email': self.email,
                'password' : self.password,
                'first_name':self.first_name,
                'last_name':self.last_name
            }
        }
        response = self.client.post(self.url, data, format='json')
        response_json = json.loads(response.content)
        self.assertEqual(201,response.status_code)
        self.assertTrue('success' in response_json)
        
# TODO: Needs to write test case for update user data
# class RetriveUserViewsTest(APITestCase):

#     def setUp(self):
#         self.url = reverse('userupdate')
#         self.url1 = reverse('token-auth')
#         self.username = "john"
#         self.email = "johnking@got.com"
#         self.password = 'popularchoice'
#         self.first_name = 'John'
#         self.last_name = 'Snow'
#         self.user = User.objects.create_superuser(
#             self.username, self.email, self.password, self.first_name, self.last_name
#         )

#     def test_user_retive_data(self):
#         data = {
#             'username': self.username,
#             'password': self.password
#         }
#         response = self.client.post(self.url1, data)
#         response_json1 = json.loads(response.content)['data']['token']
#         token = 'JWT ' + response_json1
#         response = self.client.get(self.url,**{'Authorization':token})
#         response_json = json.loads(response.content)
#         print(response_json)
#         # self.assertEqual(400,response.status_code)
#         # self.assertTrue('errors' in response_json)
#         # self.assertTrue('error' in response_json['errors'])

#     # def test_super_user_with_data(self):
#     #     data = {
#     #         'user':{
#     #             'username': self.username,
#     #             'email': self.email,
#     #             'password' : self.password
#     #         }
#     #     }
#     #     response = self.client.post(self.url3, data, format='json')
#     #     response_json = json.loads(response.content)
#     #     self.assertEqual(201,response.status_code)
#     #     self.assertTrue('success' in response_json)
