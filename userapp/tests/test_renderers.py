'''Test the renderer of authentication app.'''
from django.test import SimpleTestCase
import json

# Create your tests here.
from userapp.renderers import UserJSONRenderer


class UserappRendererTest(SimpleTestCase):
    def setUp(self):
        self.data_none = {'Hello': 'World'}
        self.data_error = {
            'errors':{
                'username': 'this is wrong'
            }
        }
        self.data_detail = {
            "detail":"Method Get not possible"
        }

        self.render_user = UserJSONRenderer()

    def test_render_if_error(self):
        ret_json = self.render_user.render(self.data_error)
        ret_dict = json.loads(ret_json)
        self.assertTrue('errors' in ret_dict)
        self.assertTrue('error' in ret_dict['errors'])

    def test_render_no_error(self):
        ret_json = self.render_user.render(self.data_none)
        ret_dict = json.loads(ret_json)
        self.assertTrue('success' in ret_dict)

    def test_render_if_detail(self):
        ret_json = self.render_user.render(self.data_detail)
        ret_dict = json.loads(ret_json)
        self.assertTrue('detail' in ret_dict)
