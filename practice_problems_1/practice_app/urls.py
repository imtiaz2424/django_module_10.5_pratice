
from django.urls import path, include
from . import views

urlpatterns = [
    path('blogs/', views.blog),
]