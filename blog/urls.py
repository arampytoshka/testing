from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('random', views.post_random, name='post_random'),
]