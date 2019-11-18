from django.urls import path

from .views import JSONWebTokenObtain,JSONWebTokenRefresh,JSONWebTokenVerify, TokenVerify

urlpatterns = [
    path('token-auth',JSONWebTokenObtain.as_view(), name='token-auth'),
    path('token-auth-refresh',JSONWebTokenRefresh.as_view(), name='token-auth-refresh'),
    path('token-auth-verify',JSONWebTokenVerify.as_view(), name='token-auth-verify'),
    path('token-verify', TokenVerify.as_view(), name='token-verify'),
]