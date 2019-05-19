import json

from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key, related

from reporter.models import Report

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from userapp.models import User

from state.views import schemaWrite, schemaUpdate, schemaOpen, schemaDelete

class SchemaWriteTest(TestCase):

    def setUp(self):
        self.url = reverse('schema-write')
        self.url1 = reverse('token-auth')
        # self.url2 = reverse('')
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
        self.report_data =  Recipe(Report,
            report_type ="vessel",
            author = "john",
            projectName = "ironthrone",
            orientation = "vertical",
            location_state = 'states/user_john/ironthrone/data.json',
            location = 'reports/user_john/'
        )

    def test_schema_write_without_authorization_token(self):
        data = {}
        response = self.client.post(self.url,data,format=json)
        response_json = json.loads(response.content)
        self.assertEqual(401, response.status_code)
        self.assertTrue('detail' in response_json)

    def test_schema_write_with_authorization_token(self):
        reports = self.report_data.make()
        data = {
            'schema': {[
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
            ]
            },
            'projectID':reports.id
        }
        response = self.client.post(self.url,data,format=json,**{'HTTP_AUTHORIZATION':'JWT '+self.token})
        response_json = json.loads(response.content)
        print(response_json)
        self.assertEqual(401, response.status_code)
        self.assertTrue('detail' in response_json)