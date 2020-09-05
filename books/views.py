from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from books.models import Book


def home_page(request):
    books = Book.objects.all()

    html = render_to_string("home.html", {"books": books})
    return HttpResponse(content=html)


def book_page(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "book.html", {
        "book": book
    })
