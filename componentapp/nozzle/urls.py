from django.urls import path
from .views import NozzleAPIView

app_name = 'nozzle'
urlpatterns = [
    path('nozzle/data',NozzleAPIView.as_view()),
]
