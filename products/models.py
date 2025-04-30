from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    production_date = models.DateField()
    cost = models.IntegerField()
    in_stock = models.BooleanField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
        db_table = 'products'
