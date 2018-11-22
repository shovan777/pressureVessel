from django.urls import path
from . import views

app_name = 'cylinder'
urlpatterns = [
    path('api/cylinder/', views.ParameterListCreate.as_view()),
    path('api/cylinder/<int:thickness>/', views.results, name='results'),
    path('api/data/', views.data, name='data'),
    path('api/csrf/', views.csrf),
    path('api/ping/', views.ping),
]
