from django.urls import path
from . import views

urlpatterns = [
    # Only an empty string will match; tells django that
    # views.post_list is place to go at blank url
    path('', views.post_list, name='post_list'),
    path('post/(<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/(<int:pk>/edit/', views.post_edit, name='post_edit'),
]
