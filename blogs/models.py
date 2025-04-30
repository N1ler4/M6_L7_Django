from django.db import models

# Create your models here.


class Blog(models.Model):

    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
    author = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'
        db_table = 'blogs'