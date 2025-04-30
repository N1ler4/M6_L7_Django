from django.urls import path
from .views import base , books_app , books_detail
# from .views import

urlpatterns = [
    path('', base, name='base'),
    path('books' , books_app, name='books'),
    path('books/<int:book_id>/' , books_detail, name='books_detail')
]
