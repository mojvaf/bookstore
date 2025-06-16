from django import forms
from ..models.book import Book
from ..models.book import Author
from ..models.book import Publisher

class CreateBookForm(forms.Form):
   class Meta:
      model = Book
      fields = ['name','publisher','author','review']

      Publisher = forms.ModelChoiceField(
         queryset= Publisher.objects.all(),
         label='Publisher',
         required=False
      )

      Author = forms.ModelChoiceField(
         queryset= Author.objects.all(),
         label= 'Author',
         required=False
      )