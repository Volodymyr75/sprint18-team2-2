from django.shortcuts import render
from rest_framework import generics
from .serializers import BookDetailSerializer
from .models import Book

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer

class BookListView(generics.ListAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
