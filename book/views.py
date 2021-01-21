from django.shortcuts import render, redirect
from .models import Book, Author
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from .forms import BookForms


def all_books(request):
    books = list(Book.objects.all())
    context = {'books': books}
    return render(request, 'book/all_books.html', context)


def book_by_id(request, id=0):
    book_by_id = Book.objects.get(id=id)
    return render(request, 'book/book_by_id.html', {'title': "Book by id", "book_by_id": book_by_id})


def update_by_id(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForms()
        else:
            book = Book.objects.get(pk=id)
            form = BookForms(instance=book)
        return render(request, 'book/update_by_id.html', {'form': form})

    if request.method == 'POST':
        if id == 0:
            form = BookForms(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForms(request.POST, instance=book)
        form.save()
        return redirect('books')


def book_delete(request, id=0):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('books')
