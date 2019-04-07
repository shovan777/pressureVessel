"""Render lifting lug data."""
import json

from rest_framework.renderers import JSONRenderer


class LiftingLugJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        errors = data.get('errors', None)
        detail = data.get('detail', None)

        if detail is not None:
            return super(LiftingLugJSONRenderer, self).render(data)

        if errors is not None:
            return super(LiftingLugJSONRenderer, self).render(data)

        return json.dumps(data['response'])
