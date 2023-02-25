from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from .forms import *
from .models import Book
import requests

# Create your views here.

class HomeView(TemplateView):
    template_name = 'books/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class AllBooksView(TemplateView):
    context_object_name = 'book'
    template_name = 'books/all_books.html'
    model = Book

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        return {'books': Book.objects.all()}


class AddBooksView(TemplateView):
    template_name = 'books/add_books.html'
    error_template = 'books/error.html'
    model = Book
    add_form = AddBookForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['add_form'] = self.add_form()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        add_form = self.add_form(request.POST)
        if add_form.is_valid():
            form_data = add_form.cleaned_data
            book = self.model.objects.create(**form_data)
            book.save()
            return HttpResponseRedirect(reverse('books:add_books', args=args))
        else:
            return render(request, self.error_template, {'errors': add_form.errors})


class ImportBooksView(TemplateView):
    template_name = 'books/import_books.html'

    def get(self, request, *args, **kwargs):
        context = {}

        if 'search' in str(request.GET):
            print(request.GET)
            context.update(self.get_context_data(search_query=request.GET['search_query']))

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)

    def get_context_data(self, **kwargs):
        query = kwargs['search_query']
        link = f'https://www.googleapis.com/books/v1/volumes?q={query}'
        data = requests.get(link).json()['items']
        return {'results': data}









