# django modules
from django.urls import include, path
from django.conf.urls import url

# django-rest-framework modules
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# state modules
from . import views
from .views import schemaWrite, schemaUpdate, schemaOpen, schemaDelete

router = routers.DefaultRouter()

router.register(r'cylinderstates', views.CylinderStateViewSet)
router.register(r'nozzlestates', views.NozzleStateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('state/write', schemaWrite, name='schema-write'),
    path('state/update', schemaUpdate, name='schema-update'),
    path('state/open', schemaOpen, name='schema-open'),
    path('state/delete', schemaDelete, name='schema-delete'),
]