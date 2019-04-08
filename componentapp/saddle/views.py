from .serializers import ParameterSerializer
from .renderers import ParameterJSONRenderer
from .utils.saddleCalc import skirtCalc

# django-rest modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class SaddleResponse(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_classes = ParameterSerializer
    renderer_classes = (ParameterJSONRenderer,)
    def post(self, request, format=None):
        data = request.data.get('saddleParam',{})
        data['projectID'] = request.data.get('projectID',None)
        serializer = self.serializer_classes(data=data)
        serializer.is_valid(raise_exception=True)
        data1 = serializer.data

        responses = skirtCalc()

        return Response(serializer.data,status=status.HTTP_200_OK)
