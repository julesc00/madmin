from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name="posts"),
    path('categories/', views.categories, name="categories"),
    path('comments/', views.comments, name="comments"),
    path('users/', views.users, name="users"),
    path('test/', views.test, name="test"),
]