from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.AllBooksView)
router.register(r'search', views.SearchBooksView)
router.register(r'date', views.FilteredByDate)

app_name = 'restapi'
urlpatterns = [
    path('', include(router.urls)),
    ]

