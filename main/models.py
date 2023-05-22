from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    publication_date = models.DateField()
    cover_photo = models.ImageField(upload_to='media/')
