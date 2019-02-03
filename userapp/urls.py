from django.urls import path

from .views import RegistrationNormalUserAPIView,UserRetrieveUpdateAPIView,RegistrationSuperUserAPIView

urlpatterns = [
    path('user-update',UserRetrieveUpdateAPIView.as_view()),
    path('user-create',RegistrationNormalUserAPIView.as_view()),
    path('superuser-create',RegistrationSuperUserAPIView.as_view()),
]