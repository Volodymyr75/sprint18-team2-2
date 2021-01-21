from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author
from django.core.exceptions import ObjectDoesNotExist


def author_list(request):
    context = {'title': "All authors", "authors": Author.objects.all()}
    return render(request, 'author/all_authors.html', context)


def author_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
            return render(request, 'author/author_form.html', {'form': form, 'operation': 'creation'})
        else:
            author = Author.get_by_id(id)
            if author is None:
                raise FileNotFoundError
            if request.path.startswith('/author/edit'):
                form = AuthorForm(instance=author)
                return render(request, 'author/author_form.html', {'form': form, 'operation': 'editing'})
        return render(request, 'author/author_by_id.html', {'author_by_id': author})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.get_by_id(id)
            if author is None:
                raise ObjectDoesNotExist
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'author/author_form.html', {'form': form})
        return redirect('author_list')


# Create your views here.

def author_by_id(request, id=0):
    author_by_id = Author.objects.get(id=id)
    return render(request, 'author/author_by_id.html', {'title': "Author by id", "author_by_id": author_by_id})


def author_delete(request, id=0):
    author = Author.get_by_id(id)
    if author is None:
        raise ObjectDoesNotExist
    author.delete()
    return redirect('author_list')
