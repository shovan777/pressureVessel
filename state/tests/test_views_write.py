import json

from django.urls import reverse
from django.test import TestCase

from userapp.models import User

from pressureVessel import settings

import shutil

class SchemaWriteTest(TestCase):

    def setUp(self):
        self.url = reverse('schema-write')
        self.url1 = reverse('token-auth')
        self.url2 = reverse('report-list')

        self.user = User.objects.create_superuser(
            username="john",
            email="johnking@got.com",
            password="popularchoice",
            first_name="John",
            last_name="Snow"
        )
        self.data1 = {
            'username':'john',
            'password':'popularchoice'
        }
        self.token = json.loads(self.client.post(self.url1, self.data1).content)['data']['token']
    
    def tearDown(self):
        shutil.rmtree(settings.STATIC_ROOT+"/states/user_john/1", ignore_errors=True)
        shutil.rmtree(settings.STATIC_ROOT+"/states/user_john/2", ignore_errors=True)
        shutil.rmtree(settings.STATIC_ROOT+"/states/user_john/3", ignore_errors=True)
        
    def test_schema_write_without_authorization_token(self):
        data_report = {
            "report_type":"vessel",
            "projectName":"1",
            "orientation":"vertical"
        }
        response_report = json.loads(self.client.post(self.url2,data_report,format=json,**{'HTTP_AUTHORIZATION':'JWT '+self.token}).content).get('id')
        data = {
            "schema": {
                "component": "Cylinder",
                "type": "blob",
                "componentID": 0,
                "componentName": "2",
                "material": "SA-516 60",
                "ip": 300,
                "temp1": 300,
                "ep": "15",
                "temp2": "300",
                "ic": "0.125",
                "sd": 72,
                "length": "8",
                "thickness": 0.775,
                "number": 1,
                "spec_num": "SA-516",
                "type_grade": "60",
                "value": {
                    "thickness": 0.7655141843971631,
                    "weight": 1952.38476084217
                }
            },
            "projectID": response_report
        }
        response = self.client.post(self.url,data,format=json)
        response_json = json.loads(response.content)
        self.assertEqual(401, response.status_code)
        self.assertTrue('detail' in response_json)

    def test_schema_write_with_authorization_token(self):
        data_report = {
            "report_type":"vessel",
            "projectName":"2",
            "orientation":"vertical"
        }
        response_report = json.loads(self.client.post(self.url2,data_report,format=json,**{'HTTP_AUTHORIZATION':'JWT '+self.token}).content).get('id')
        
        data = {
            "schema": {
                "component": "Cylinder",
                "type": "blob",
                "componentID": 0,
                "componentName": "2",
                "material": "SA-516 60",
                "ip": 300,
                "temp1": 300,
                "ep": "15",
                "temp2": "300",
                "ic": "0.125",
                "sd": 72,
                "length": "8",
                "thickness": 0.775,
                "number": 1,
                "spec_num": "SA-516",
                "type_grade": "60",
                "value": {
                    "thickness": 0.7655141843971631,
                    "weight": 1952.38476084217
                }
            },
            "projectID": response_report
        }
        response = self.client.post(self.url,data,content_type="application/json",format=json,**{'HTTP_AUTHORIZATION':'JWT '+self.token})
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'ok iam writing', response.content)

    def test_schema_write_without_projectid(self):
        data_report = {
            "report_type":"vessel",
            "projectName":"3",
            "orientation":"vertical"
        }
        response_report = json.loads(self.client.post(self.url2,data_report,format=json,**{'HTTP_AUTHORIZATION':'JWT '+self.token}).content).get('id')
        data = {
            "schema": {
                "component": "Cylinder",
                "type": "blob",
                "componentID": 0,
                "componentName": "2",
                "material": "SA-516 60",
                "ip": 300,
                "temp1": 300,
                "ep": "15",
                "temp2": "300",
                "ic": "0.125",
                "sd": 72,
                "length": "8",
                "thickness": 0.775,
                "number": 1,
                "spec_num": "SA-516",
                "type_grade": "60",
                "value": {
                    "thickness": 0.7655141843971631,
                    "weight": 1952.38476084217
                }
            }
        }
        resp = self.client.post(self.url,data,format=json,content_type="application/json",**{'HTTP_AUTHORIZATION':'JWT '+self.token})
        response_json = json.loads(resp.content)
        self.assertEqual(400, resp.status_code)
        self.assertTrue('errors' in response_json)