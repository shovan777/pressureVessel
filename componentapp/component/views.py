from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions

# component modules
from .models import Component
from .serializer import ComponentSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    permission_clases = (permissions.IsAuthenticated,)
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        serializer.save(
            report_id = self.request.data.get('projectID', 88)
        )