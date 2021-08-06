from django.urls import path
from . import views
"""post/ means, that after start URL we will get URL started with post and /.
    <int:pk> means, that Django waits int and transforms it in var - pk.
     '/' - symbol in end of URL."""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]