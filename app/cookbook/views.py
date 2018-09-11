from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


from .models import Book


def my_view(request):
    posts = cache.get('posts')
    if not posts:
        posts = list(Book.objects.all().values('id', 'text'))
        cache.set('posts', posts)
    return JsonResponse(posts, safe=False)