from django.urls import path

from .views import RegistrationNormalUserAPIView,UserRetrieveUpdateAPIView,RegistrationSuperUserAPIView

urlpatterns = [
    path('user-update',UserRetrieveUpdateAPIView.as_view(),name="userupdate"),
    path('user-create',RegistrationNormalUserAPIView.as_view(),name="usercreate"),
    path('superuser-create',RegistrationSuperUserAPIView.as_view(),name="superusercreate"),
]