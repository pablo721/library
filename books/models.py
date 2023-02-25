from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    pub_date = models.DateField()
    isbn = models.CharField(max_length=13)
    n_pages = models.IntegerField()
    cover_link = models.CharField(max_length=64)
    language = models.CharField(max_length=16)


