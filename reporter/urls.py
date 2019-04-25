# django modules
from django.urls import include, path
from django.conf.urls import url

# django-rest-framework modules
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns

# reporter modules
from . import views
from .views import ReportViewSet


# project_data = ReportViewSet.as_view({
#     'get': 'project'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

router = routers.DefaultRouter()
router.register(r'reports', views.ReportViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('generate', views.index, name='index'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)