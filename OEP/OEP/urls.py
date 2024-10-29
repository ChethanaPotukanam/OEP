from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.BASE, name="home"),  # Root URL pattern
    path("base", views.BASE, name="base"),
]
