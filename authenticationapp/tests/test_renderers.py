'''Test the renderer of authentication app.'''
from django.test import SimpleTestCase
import json

# Create your tests here.
from authenticationapp.renderers import JSONTokenRenderer


class AuthRendererTest(SimpleTestCase):
    def setUp(self):
        self.data_none = {'Hello': 'World'}
        self.data_error = {
            'errors': 'this is wrong'
        }

        self.render_token = JSONTokenRenderer()

    def test_render_if_error(self):
        ret_json = self.render_token.render(self.data_error)
        ret_dict = json.loads(ret_json)
        self.assertFalse('data' in ret_dict)

    def test_render_no_error(self):
        ret_json = self.render_token.render(self.data_none)
        ret_dict = json.loads(ret_json)
        self.assertTrue('data' in ret_dict)
