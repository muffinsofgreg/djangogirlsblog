from django.conf.urls import url
from . import views

urlpatterns = [
    # Only an empty string will match; tells django that
    # views.post_list is place to go at blank url
    url(r'^$', views.post_list, name='post_list'),
]
