from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date', 'isbn', 'n_pages', 'cover_link', 'language']

