from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/<int:pk>/', views.postpage, name='post'),
]

