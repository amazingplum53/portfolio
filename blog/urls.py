from django.urls import path

from . import views

urlpatterns = [

    path('featured/', views.featured),
    
    path('article/<int:article_id>', views.article),

]