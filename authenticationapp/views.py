from rest_framework_jwt.views import ObtainJSONWebToken,RefreshJSONWebToken,VerifyJSONWebToken
from rest_framework import status
from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer,RefreshJSONWebTokenSerializer,VerifyJSONWebTokenSerializer
)
from .renderers import (
    JSONTokenRenderer
)
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

class JSONWebTokenObtain(ObtainJSONWebToken):

    serializer_class = JSONWebTokenSerializer
    renderer_classes = (JSONTokenRenderer,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.object.get('user') or request.user
        token = serializer.object.get('token')
        response_data = jwt_response_payload_handler(token=token, request=request)
        return Response(response_data,status=status.HTTP_200_OK)

class JSONWebTokenRefresh(RefreshJSONWebToken):

    renderer_classes = (JSONTokenRenderer,)

    def validate(self, attrs):
        return super(RefreshJSONWebTokenSerializer,self).validate(attrs)

class JSONWebTokenVerify(VerifyJSONWebToken):
    
    renderer_classes = (JSONTokenRenderer,)

    def validate(self, attrs):
        return super(VerifyJSONWebTokenSerializer,self).validate(attrs)