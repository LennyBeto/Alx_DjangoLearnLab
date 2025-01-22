

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from django.urls import path
from .views import FollowUser, UnfollowUser, FeedView

class FollowUser(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.all()
        request.user.following.add(user_to_follow)
        return Response({"message": "You are now following this user."})

class UnfollowUser(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.all()
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "You have unfollowed this user."})
    
urlpatterns = [
    path('follow/<int:user_id>/', FollowUser.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view(), name='unfollow_user'),
    path('feed/', FeedView.as_view(), name='user_feed'),
]
