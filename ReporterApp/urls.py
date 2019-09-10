from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = "PressureVesselApp"

urlpatterns = [
    # path('', GeneratePdfView.as_view(), name='generatepdf'),
    # path('generate/',views.index, name='generate'),
    path('', GeneratePdf.as_view(), name='generatepdf'),
    path('pdf/', views.PdfGeneration, name='pdfgeneration'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
