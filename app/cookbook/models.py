from django.core.cache import cache
from django.db import models


# Create your models here.

class Book(models.Model):
    text = models.TextField()

    def save(self, *args, **kwargs):
        cache.delete('posts')
        print('saved')
        super().save(*args,**kwargs)

    def delete(self, *args, **kwargs):
        cache.delete('posts')
        super().delete(*args,**kwargs)

    def __str__(self):
        return self.text
