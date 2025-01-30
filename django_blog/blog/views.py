from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUser CreationForm
from .models import Post

# Authentication Views
def register(request):
    if request.method == 'POST':
        form = CustomUser CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUser CreationForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})

# Blog Post Views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Specify your template name
    context_object_name = 'posts'  # Default is 'object_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    context_object_name = 'post'  

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content', 'author'] 
    success_url = reverse_lazy('post-list')  

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # Specify your template name
    fields = ['title', 'content']  # Specify the fields to include in the form
    success_url = reverse_lazy('post-list')  # Redirect after successful update

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Specify your template name
    success_url = reverse_lazy('post-list') 
