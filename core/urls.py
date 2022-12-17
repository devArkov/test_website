from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
]
