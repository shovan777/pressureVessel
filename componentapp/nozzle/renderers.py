import json

from rest_framework.renderers import JSONRenderer


class NozzleJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        
        errors = data.get('errors', None)
        detail = data.get('detail',None)

        if detail is not None:
            return super(NozzleJSONRenderer,self).render(data)

        if errors is not None:
            return super(NozzleJSONRenderer,self).render(data)
        
        data.pop('id')
        if data['type_name'] == 'LWN':
            data.pop('nut_relief_diameter')
            data.pop('nut_relief_length')
        
        data.pop('type_name')
        data.pop('class_value')
        data.pop('nominal_pipe_size')
        data.pop('spec_num')
        data.pop('type_grade')
        data.pop('temp1')
        data.pop('designPressure')
        data.pop('cylinderDiameter')
        data.pop('corrosionAllowance')
        data.pop('cylinderThickness')
        data.pop('nozzleDiameter')
        data.pop('externalNozzleProjection')
        data.pop('internalNozzleProjection')
        data.pop('projectID')

        return json.dumps(data)