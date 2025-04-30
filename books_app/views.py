from django.shortcuts import render
from .models import Book

# Create your views here.

def base(request):
    return render(request, 'base.html')

def books_app(request):

    books_db = Book.objects.all()

    return render(request=request, template_name='books/books.html', context={'books': books_db})

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request=request, template_name='books/book_detail.html', context={'book': book})
