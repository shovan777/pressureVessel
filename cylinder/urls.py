from django.urls import path
from . import views

app_name = 'cylinder'
urlpatterns = [
    path('data/', views.data, name='data'),
]
