from django import forms
from .models import Book, Author, Publisher


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'cover_photo']


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']


class AddPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']
