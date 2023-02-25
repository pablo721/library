from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all_books/', views.AllBooksView.as_view(), name='all_books'),
    path('add_books/', views.AddBooksView.as_view(), name='add_books'),
    path('import_books/', views.ImportBooksView.as_view(), name='import_books'),
    ]

