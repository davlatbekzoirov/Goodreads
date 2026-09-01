from django.shortcuts import render
from django.views import View
from .models import Book

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()

        return render(request, 'books/list.html', {"books": books})