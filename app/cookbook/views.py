from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Book


def my_view(request):
    posts = Book.objects.all().values('id', 'text')
    return JsonResponse(list(posts), safe=False)
