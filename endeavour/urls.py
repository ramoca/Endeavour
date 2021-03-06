"""endeavour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('Apps.Landing.urls')),

    url(r'^inventory/', include('Apps.Inventory.urls')),
    url(r'^shop/', include('Apps.Shop.urls')),
    url(r'^users/', include('Apps.Users.urls')),

    url(r'^login/', 'Apps.Users.views.signin', name='entrar'),
    url(r'^logout/', 'Apps.Users.views.log_out', name='salir'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)