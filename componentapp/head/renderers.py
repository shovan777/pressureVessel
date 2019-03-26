import json

from rest_framework.renderers import JSONRenderer


class HeadJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        errors = data.get('errors', None)
        detail = data.get('detail',None)    

        if detail is not None:
            return super(HeadJSONRenderer,self).render(data)

        if errors is not None:
            return super(HeadJSONRenderer,self).render(data)
        
        return json.dumps({
            'thickness':data['thickness'],
            'MAWP':data['MAWP'],
            'MAWPResponse':data['MAWPResponse'],
            'weight':data.get('weight',0),
            'weightTimesCG':data.get('weightTimesCG',0)
        })