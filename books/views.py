from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,  DetailView
from .models.book import Book

class BooksPage(ListView):
    template_name =  'books.html'
    model = Book
    context_object_name = 'books_list'


class BookDetailview(DetailView):
    template_name = 'book_details.html'
    model = Book
    context_object_name = 'book'
