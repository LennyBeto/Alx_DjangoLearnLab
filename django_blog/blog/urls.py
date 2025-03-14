from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update an existing post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]
