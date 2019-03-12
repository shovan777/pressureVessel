from django.urls import path
from .views import SkirtThicknessData
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'skirt'
urlpatterns = [
    path('skirt/data', SkirtThicknessData.as_view(), name='skirtData'),
]
urlpatterns = format_suffix_patterns(urlpatterns)