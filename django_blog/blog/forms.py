from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post 
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
       email = forms.EmailField(required=True)

       class Meta:
           model = User
           fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title', 'content']  # Include fields you want to display

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
    
