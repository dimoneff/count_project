from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('count/', views.count, name='count'),
    path('show/', views.show, name='show'),
    path('about/', views.about, name='about'),
]