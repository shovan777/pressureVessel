import json

from rest_framework.renderers import JSONRenderer


class NozzleJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        response = data.get('responses')

        errors = data.get('errors', None)
        detail = data.get('detail', None)

        if detail is not None:
            return super(NozzleJSONRenderer,self).render(data)

        if errors is not None:
            return super(NozzleJSONRenderer,self).render(data)
        
        response.pop('id')
        if response['type_name'] == 'LWN':
            response.pop('nut_relief_diameter')
            response.pop('nut_relief_length')
        
        response.pop('type_name')
        response.pop('class_value')
        response.pop('nominal_pipe_size')

        return json.dumps(response)