"""bricks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from bricksapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('index/', views.home_view, name='home'),
    path('form-success/', views.form_success_view, name='form_success'),
    path('visa-embassy-guidance/', views.visa_embassy_view, name='visa_embassy_view'),
    path('airport-pickup/', views.airport_pickup_view, name='airport_pickup'),
    path('application-assistance/', views.application_assistance_view, name='application_assistance'),
    path('university-requirements/', views.universities_view, name='partner_institutions'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
