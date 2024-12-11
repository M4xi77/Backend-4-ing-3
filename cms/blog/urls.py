from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
    
    path('home_page/',views.main_page,name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/edit/', views.edit_blog, name='edit_blog'),
    path('blog/<int:pk>/delete/', views.delete_blog, name='delete_blog'),
    path('blogs/', views.blog_list, name='blog_list'),
]
