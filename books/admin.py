from django.contrib import admin
from .models.book import Book,  Publisher, Author

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)