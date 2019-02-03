from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from emailapp.funcs import SendEmailVerification

from .serializers import (
    RegistrationNormalUserSerializer, UserSerializer,RegistrationSuperUserSerializer
)
from .renderers import UserJSONRenderer


class RegistrationNormalUserAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationNormalUserSerializer

    def post(self, request):
        user = request.data.get('user',{})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        SendEmailVerification(user={
            'username':serializer.data.get('username'),
            'pk':serializer.data.get('pk'),
            'is_active':serializer.data.get('is_active'),
            'email':serializer.data.get('email'),
        },request=request)        

        return Response(serializer.data,status=status.HTTP_201_CREATED)

class RegistrationSuperUserAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSuperUserSerializer

    def post(self, request):
        user = request.data.get('user',{})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user',{})

        serializer = self.serializer_class(
            request.user, data= serializer_data, partial =True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)