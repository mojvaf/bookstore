from django import forms
from ..models.book import Author
from ..models.book import Publisher
from ..models.book import Book
from ..models.contact import Contact

class CreateBookForm(forms.Form):
      name = forms.CharField(max_length=20)

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


class BookForm(forms.ModelForm):
      class Meta:
            model = Book
            fields = ['name','author', 'publisher', 'review']

            

class ContactForm(forms.ModelForm):
     class Meta:
           model = Contact
           fields = ['name', 'content']
           widgets = {'name': forms.TextInput(attrs = {'class': 'form-control'})}
      