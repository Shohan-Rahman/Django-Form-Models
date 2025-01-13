from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name = 'app'),
    path('about/', views.about, name = 'about'),
    path('form/', views.submit, name = 'form'),
]