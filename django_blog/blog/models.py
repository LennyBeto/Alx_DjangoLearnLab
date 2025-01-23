

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from .models import Post

class Post(models.Model):
       title = models.CharField(max_length=200)
       content = models.TextField()
       published_date = models.DateTimeField(auto_now_add=True)
       author = models.ForeignKey(User, on_delete=models.CASCADE)

       def __str__(self):
           return self.title
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' here

    tags = forms.CharField(required=False)  # Optional field for tags
