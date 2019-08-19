'''Test the utils of authentication app.'''
from django.test import SimpleTestCase

from authenticationapp.utils import my_jwt_response_handler

class AuthUtilsTest(SimpleTestCase):
    def setUp(self):
        self.token = 'fire'
        
    def test_my_jwt_res_handler_contains_token(self):
        ret_json = my_jwt_response_handler(self.token)
        self.assertTrue('token' in ret_json)
