from django.urls import path
from .views import like_post, unlike_post, FeedView

urlpatterns = [
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
    path('feed/', FeedView.as_view(), name='feed'),
]
