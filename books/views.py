from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,  DetailView
from .models.book import Book
from .forms.form import CreateBookForm


class BooksPage(ListView):
    template_name =  'books.html'
    model = Book
    context_object_name = 'books_list'


class BookDetailview(DetailView):
    template_name = 'book_details.html'
    model = Book
    context_object_name = 'book'


def create_book_form_view(request):
     if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            model = Book(
                name = form.cleaned_data['name'],
                author = form.cleaned_data['author'],     
                publisher = form.cleaned_data['publisher'],
                review = form.cleaned_data['review']
            )
            model.save()
            return render(request, 'form_success.html', {'name': model.name})
     else:
        form = CreateBookForm()

     return render(request, 'form_template.html', {'form':form})        


