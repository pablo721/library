from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets, filters, generics
from .serializers import BookSerializer
from books.models import Book

# Create your views here.


class AllBooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'title', 'author']




class SearchBooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'isbn', 'language', 'pub_date']



class DateFilter(django_filters.FilterSet):

    start = django_filters.rest_framework.IsoDateTimeFilter(field_name='start', lookup_expr='gte')
    end = django_filters.rest_framework.IsoDateTimeFilter(field_name='end', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['pub_date']


class FilteredByDate(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DateFilter]
    search_fields = ['pub_date']




