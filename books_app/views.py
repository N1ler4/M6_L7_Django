from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book 
# Create your views here.

def base(request):
    return render(request, 'base.html')


class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/add.html'
    fields = ['title', 'author', 'pages', 'language' , 'publication_date']
    success_url = '/books/'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/update.html'
    fields = ['title', 'author', 'pages', 'language' , 'publication_date']
    success_url = '/books/'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    context_object_name = 'book'
    success_url = '/books/'    