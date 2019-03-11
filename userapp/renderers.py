import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        errors = data.get('errors', None)
        detail = data.get('detail',None)

        if detail is not None:
            return super(UserJSONRenderer,self).render(data)

        if errors is not None:
            output = {
                'errors' : {
                    'error' : [
                    ]
                }
            }
            for x in errors:
                output['errors']['error'].append(errors.get(x)[0])
            
            return super(UserJSONRenderer,self).render(output)

        return json.dumps({
            'detail':'please validate your account',
        })