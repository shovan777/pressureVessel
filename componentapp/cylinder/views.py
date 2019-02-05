# cylinder modules
from .models import Parameter
from .serializers import ParameterSerializer
from .renderers import ParameterJSONRenderer

# django modules
from django.http import Http404, JsonResponse

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ThicknessData(APIView):
    """
    Determine thickness for provided cylinder params
    """
    # permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializer
    renderer_classes = (ParameterJSONRenderer,)
    def post(self, request, format=None):

        data = request.data.get('cylinderParam', {})
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        thickness = Parameter.objects.get_thickness(data=serializer.data)
        newdict = {'thickness':thickness}
        newdict.update(serializer.data)
        return Response(newdict,status=status.HTTP_200_OK)
