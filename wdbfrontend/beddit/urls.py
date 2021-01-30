from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('posts/<int:pk>/', views.postPage, name='post'),
]

