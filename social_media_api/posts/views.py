from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth.models import User


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

def get_object(self):
        return generics.get_object_or_404(Post, pk=pk)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer  

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        Notification.objects.create(recipient=post.user, actor=request.user, verb='liked', target=post)
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)


