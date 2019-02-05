from django.urls import path
from .views import ThicknessData
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'cylinder'
urlpatterns = [
    path('cylinder/data', ThicknessData.as_view(), name='data'),
]
urlpatterns = format_suffix_patterns(urlpatterns)