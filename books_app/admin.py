from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book


# Register your models here.

class BookAdmin(ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_per_page = 10

admin.site.register(Book, BookAdmin)
