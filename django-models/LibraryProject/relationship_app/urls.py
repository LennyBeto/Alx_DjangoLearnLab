"""
URL configuration for relationship_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
from .views import list_books
from .templates import register.html
from .templates import login.html
from .templates import logout.html
from .views import add_book, edit_book, delete_book



urlpatterns = [

    path('register/', views.register, name='register')
    path('login/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='templates/logout.html'), name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add/', add_book, name='add_book/'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book/'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book/'),
]
