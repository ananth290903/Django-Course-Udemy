from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

def index(request):
    books=Book.objects.all()
    return render(request,"book_outlet/index.html",{"books":books})

def book_detail(request,slug):
    book=get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{"title":book.title,"author":book.author,"rating":book.rating,"isBestSeller":book.isBestSeller})