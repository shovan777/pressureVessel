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
        
        return json.dumps({
            'flange_outer_diameter': data['flange_outer_diameter'],
            'flange_thickness': data['flange_thickness'],
            'raised_face_diameter': data['raised_face_diameter'],
            'blot_hole_number': data['blot_hole_number'],
            'blot_hole_size': data['blot_hole_size'],
            'blot_circle_diameter': data['blot_circle_diameter'],
            'bore': data['bore'],
            'barrel_outer_diameter': data['barrel_outer_diameter'],
            'pipe_outer_diameter_inch': data['pipe_outer_diameter_inch'],
            'pipe_internal_diameter_inch': data['pipe_internal_diameter_inch'],
            'wall_inch': data['wall_inch'],
            'est_wt': data['est_wt']
        })