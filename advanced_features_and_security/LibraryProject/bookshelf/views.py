from django.shortcuts import render
from .models import Book 

def book_list(request):
    try:
        books = Book.objects.all()  # Fetch all books from the database
        return render(request, 'bookshelf/book_list.html', {'books': books})
    except Exception as e:
        raise_exception(e)  
