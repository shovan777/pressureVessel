"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from emailapp import funcs
# del these imports done for media url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('frontend.urls')),
    path('api/', include('componentapp.component.urls')),
    path('report/', include('reporter.urls')),
    path('api/', include('componentapp.cylinder.urls')),
    path('api/', include('componentapp.head.urls')),
    path('api/', include('componentapp.nozzle.urls')),
    path('api/', include('componentapp.skirt.urls')),
    path('user/', include('userapp.urls')),
    path('admin', admin.site.urls),
    path('auth/', include('authenticationapp.urls')),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        funcs.activate, name='activate'),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
