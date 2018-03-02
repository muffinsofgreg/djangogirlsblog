from django.urls import path
from . import views

urlpatterns = [
    # Only an empty string will match; tells django that
    # views.post_list is place to go at blank url
    path('', views.post_list, name='post_list'),
    path('post/(<int:pk>/', views.post_detail, name='post_detail'),
]
