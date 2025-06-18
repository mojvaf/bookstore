from django import forms
from ..models.book import Book
from ..models.book import Author
from ..models.book import Publisher

class CreateBookForm(forms.Form):
      name = forms.CharField(max_length=255)

      publisher = forms.ModelChoiceField(
         queryset= Publisher.objects.all(),
         label='Publisher',
         required=False
      )

      author = forms.ModelChoiceField(
         queryset= Author.objects.all(),
         label= 'Author',
         required=False
      )

      review = forms.CharField(widget=forms.Textarea, required=False) 