from django.urls import path
from .views import LiftingLugAPIView

app_name = 'liftingLug'
urlpatterns = [
    path('lug/data', LiftingLugAPIView.as_view()),
]