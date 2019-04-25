# django modules
from django.urls import include, path
from django.conf.urls import url

# django-rest-framework modules
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# state modules
from . import views

router = routers.DefaultRouter()

router.register(r'cylinderstates', views.CylinderStateViewSet)
router.register(r'nozzlestates', views.NozzleStateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]