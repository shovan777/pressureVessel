from django.urls import path

from .views import RegistrationNormalUserAPIView,RegistrationSuperUserAPIView

urlpatterns = [
    # TODO: Need to be checked and update user problem updates any user
    #path('user-update',UserRetrieveUpdateAPIView.as_view(),name="userupdate"),
    path('user-create',RegistrationNormalUserAPIView.as_view(),name="usercreate"),
    path('superuser-create',RegistrationSuperUserAPIView.as_view(),name="superusercreate"),
]