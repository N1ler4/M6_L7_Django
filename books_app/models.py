from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    publication_date = models.DateField()
    pages = models.IntegerField()
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'books'