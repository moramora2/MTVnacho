from django.urls import path, include
from .views import primera_vista

urlpatterns = [path('ver_familias/', primera_vista),]

