from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Books

# Create your views here.

def index(request):
    data = Books.objects.all()
    return render(request, "index.html", context={ "books": data })


def addBook(request):
    if request.method == "POST":
        book = Books()
        book.title = request.POST['title']
        book.author = request.POST['book-author']
        book.save()
    return render(request, "index.html", context={ "books": Books.objects.all() })
