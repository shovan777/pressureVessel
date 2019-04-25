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

    def perform_create(self, serializer):
        
        if self.request.data.get('projectID') == None:
            raise newError({
            "reportError":["Report cannot be found Please Create the report"]
            })
        else:
            serializer.save(
                report_id = self.request.data.get('projectID')
            )