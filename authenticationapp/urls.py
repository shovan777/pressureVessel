from django.urls import path

from .views import JSONWebTokenObtain,JSONWebTokenRefresh,JSONWebTokenVerify

urlpatterns = [
    path('token-auth',JSONWebTokenObtain.as_view()),
    path('token-auth-refresh',JSONWebTokenRefresh.as_view()),
    path('token-auth-verify',JSONWebTokenVerify.as_view()),
]