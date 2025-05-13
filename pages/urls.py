from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('greet/<str:name>/', views.greet_view, name='greet'),
]