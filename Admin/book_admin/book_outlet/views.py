from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404
from django.db.models import Avg

# def index(request):
#     books=Book.objects.all()
#     return render(request,"book_outlet/index.html",{"books":books})



# def index(request):
#     books=Book.objects.all()
#     num_books=books.count()
#     avg_rating=books.aggregate(Avg("rating"))
#     return render(request,"book_outlet/index.html",{"books":books,"total_no_of_books":num_books,"average_rating":avg_rating})



def book_in_detail(request,slug):
    book=get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{"author":book.author,"title":book.title,"rating":book.rating,"isBestSeller":book.isBestSeller})

def index(request):
    books=Book.objects.all()
    total_no_of_books=Book.objects.all().count()
    avg_rating=books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{"books":books,"avg_rating":avg_rating,"total_no_of_books":total_no_of_books})

