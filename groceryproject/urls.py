"""
URL configuration for groceryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('groceryapp.urls')),
    path("account/",TemplateView.as_view(template_name= os.path.join(BASE_DIR,'newreact/build/index.html'))), # React page loading index.html 
    path('favicon.ico', serve, {'document_root': settings.REACT_PUBLIC_DIR, 'path': 'favicon.ico'}, name='favicon'),# To load favicon 4 react page
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
