from django.urls import path
from .views import ThicknessData,ThicknessDataConical
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'cylinder'
urlpatterns = [
    path('cylinder/data', ThicknessData.as_view(), name='data'),
    path('conicalCylinder/data',ThicknessDataConical.as_view(), name='conicaldata'),
]
urlpatterns = format_suffix_patterns(urlpatterns)