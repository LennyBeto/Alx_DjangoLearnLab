
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from django.views.generic import ListView
from .models import Post
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from .models import Post


@login_required
def profile_view(request):
       if request.method == 'POST':
           request.user.email = request.POST['email']
           request.user.save()
           return redirect('profile')
       return render(request, 'registration/profile.html', {'user': request.user})

def register(request):
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()
               login(request, user)
               return redirect('profile')
       else:
           form = CustomUserCreationForm()
       return render(request, 'registration/register.html', {'form': form})

def user_login(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('profile')
           else:
               return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
       return render(request, 'registration/login.html')

def user_logout(request):
       logout(request)
       return redirect('login')

class PostListView(ListView):
       model = Post
       template_name = 'blog/post_list.html'  # Specify your template name
       context_object_name = 'posts'

class PostDetailView(DetailView):
       model = Post
       template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
       model = Post
       form_class = PostForm
       template_name = 'blog/post_form.html'
       success_url = '/posts/'  # Redirect after creation

class PostUpdateView(UserPassesTestMixin, UpdateView):
       model = Post
       form_class = PostForm
       template_name = 'blog/post_form.html'

       def test_func(self):
           post = self.get_object()
           return self.request.user == post.author
       
class PostDeleteView(UserPassesTestMixin, DeleteView):
       model = Post
       template_name = 'blog/post_confirm_delete.html'
       success_url = '/posts/'

       def test_func(self):
           post = self.get_object()
           return self.request.user == post.author
       
def form_valid(self, form):
   form.instance.author = self.request.user
   return super().form_valid(form)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

class CommentCreateView(CreateView):
    model = Comment
    # Add your fields and success URL here
template_name = 'blog/post_detail.html'
       success_url = '/posts/'

class CommentUpdateView(UpdateView):
    model = Comment
    # Add your fields and success URL here

class CommentDeleteView(DeleteView):
    model = Comment
    # Add your success URL here

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('post_detail', post_id=comment.post.id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', post_id=comment.post.id)

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)).distinct()
    return render(request, 'search_results.html', {'results': results})
