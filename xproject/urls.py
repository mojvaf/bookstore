
from django.contrib import admin
from django.urls import path
from books.views import BooksPage, BookDetailview , create_book_form_view, book_form_view, contact_form_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',BooksPage.as_view(), name = 'books_list'),
    path("books/<int:pk>/", BookDetailview.as_view(), name="book_detail"),
    path('create-book/', create_book_form_view, name='create_book_form_view'),
    path('add-book/', book_form_view, name='book_form'),
    path('contact/', contact_form_view, name='contact_form'),
]
