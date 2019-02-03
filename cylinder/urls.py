from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'cylinder'
urlpatterns = [
    path('data/', views.ThicknessData.as_view(), name='data'),
]
urlpatterns = format_suffix_patterns(urlpatterns)