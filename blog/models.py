from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=10, default=" ")

    def __str__(self):
        return self.title
