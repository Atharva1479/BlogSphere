from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('create/', views.create_post, name='create_post'), 
]
