# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from jsonb.emporium import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # Your stuff: custom urls includes go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
