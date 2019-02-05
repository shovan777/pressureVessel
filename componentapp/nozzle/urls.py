from django.urls import path
from .views import NozzleData

app_name = 'nozzle'
urlpatterns = [
    path('nozzle/data',NozzleData.as_view()),
]
