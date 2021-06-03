from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subtraction/', views.subtraction, name='subtraction'),
    path('addition/', views.addition, name='addition'),
    path('multiplication/', views.multiplication, name='multiplication'),
    path('division/', views.division, name='division'),
]