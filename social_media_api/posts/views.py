from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return generics.get_object_or_404(Post, pk=self.kwargs['pk'])


