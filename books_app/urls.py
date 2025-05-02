from django.urls import path
from .views import BookListView , base ,BookDetailView, BookCreateView , BookUpdateView , BookDeleteView
# from .views import

urlpatterns = [
    path('', base, name='base'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='books_detail'),
    path('books/add/', BookCreateView.as_view(), name='add'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='delete'),
    # path('books' , books_app, name='books'),
    # path('books/<int:book_id>/' , books_detail, name='books_detail')
]
