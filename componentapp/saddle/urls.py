from django.urls import path
from .views import SaddleResponse
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'saddle'
urlpatterns = [
    path('saddle/data', SaddleResponse.as_view(), name='saddledata'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
