
from django.contrib import admin
from django.urls import path
from books.views import BooksPage
from books.views import BookDetailview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',BooksPage.as_view(), name = 'books_list'),
    path("books/<int:pk>/", BookDetailview.as_view(), name="book_detail"),
]
