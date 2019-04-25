# django modules
from django.urls import include, path
from django.conf.urls import url

# django-rest-framework modules
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# reporter modules
from . import views


router = routers.DefaultRouter()
router.register(r'reports', views.ReportViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('generate', views.index, name='index'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)