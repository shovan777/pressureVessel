from django.urls import path
from .views import ThicknessData
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'head'
urlpatterns = [
    path('head/data', ThicknessData.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)