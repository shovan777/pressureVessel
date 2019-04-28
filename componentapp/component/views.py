from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions

# component modules
from .models import Component
from .serializer import ComponentSerializer,ComponentInputSerializer

from exceptionapp.exceptions import newError

class ComponentViewSet(viewsets.ModelViewSet):
    permission_clases = (permissions.IsAuthenticated,)
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    serializerClass = ComponentInputSerializer

    # # override the destroy action
    # def destroy(self, request, *args, **kwargs):
    #     # username = self.request.user.username
    #     # react_component_id = self.request.data['componentID']
    #     # report_id = self.request.data['projectID']
    #     # print('****************')
    #     # print(username)
    #     # instance = self.queryset.filter(report_id=report_id).filter(react_component_id=react_component_id)[0]
    #     # # print(self.queryset)
    #     # self.queryset = temp_query
    #     print('***********')
    #     print(list(args))
    #     print(kwargs['pk'])
    #     return Response('jai papa')

    


    def perform_create(self, serializer):

        serializers = self.serializerClass(data=self.request.data)
        serializers.is_valid(raise_exception=True)
        data1 = serializers.data

        serializer.save(
            report_id=data1['projectID']
        )
        