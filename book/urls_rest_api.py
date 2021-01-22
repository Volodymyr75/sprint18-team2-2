from django.urls import path, include
from .views_rest_api import BookCreateView, BookListView, BookDetailView

urlpatterns = [
    path('create', BookCreateView.as_view()),
    path('all', BookListView.as_view()),
    path('detail/<int:pk>/', BookDetailView.as_view())
]