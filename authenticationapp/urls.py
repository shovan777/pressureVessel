from django.urls import path

from .views import JSONWebTokenObtain,JSONWebTokenRefresh,JSONWebTokenVerify

urlpatterns = [
    path('token-auth',JSONWebTokenObtain.as_view(), name='token-auth'),
    path('token-auth-refresh',JSONWebTokenRefresh.as_view(), name='token-auth-refresh'),
    path('token-auth-verify',JSONWebTokenVerify.as_view(), name='token-auth-verify'),
]