from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date', 'isbn', 'n_pages', 'cover_link', 'language']
        widgets = {
            'pub_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }



class EditBookForm(forms.Form):
    book = forms.ChoiceField(choices=())
    title = forms.CharField(max_length=32)
    author = forms.CharField(max_length=32)
    pub_date = forms.DateField()
    isbn = forms.CharField(max_length=13)
    n_pages = forms.IntegerField()
    cover_link = forms.CharField(max_length=32)
    language = forms.ChoiceField(choices=())


class ImportBookForm(forms.Form):
    pass


class SearchBookForm(forms.Form):
    pass




