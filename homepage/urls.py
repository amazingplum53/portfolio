from django.urls import path

from . import views

urlpatterns = [

    path('about/', views.home, name = 'index'),

    path('contact/', views.contact, name = 'contact'),

    path('projects/', views.projects, name = 'projects'),

]