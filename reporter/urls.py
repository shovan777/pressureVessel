# django modules
from django.urls import include, path

# django-rest-framework modules
from rest_framework import routers

# reporter modules
from . import views

router = routers.DefaultRouter()
router.register(r'reports', views.ReportViewSet)
router.register(r'cylinderstates', views.CylinderStateViewSet)
router.register(r'nozzlestates', views.NozzleStateViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('generate', views.index, name='index'),
]