# django modules
from django.urls import include
from django.conf.urls import url

# django-rest-framework modules
from rest_framework import routers

# component modules
from . import views

router = routers.DefaultRouter()
router.register(r'components', views.ComponentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]