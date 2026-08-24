from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=17)


class 