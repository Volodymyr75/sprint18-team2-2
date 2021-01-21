from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm
from django.core.exceptions import ObjectDoesNotExist


def user_list(request):
    context = {'title': "All users", "users": CustomUser.objects.all()}
    return render(request, 'user/all_users.html', context)

def user_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
            return render(request, 'user/user_form.html', {'form': form, 'operation': 'creation'})
        else:
            user = CustomUser.get_by_id(id)
            if user is None:
                raise ObjectDoesNotExist
            if request.path.startswith('/user/edit'):
                form = UserForm(instance=user)
                return render(request, 'user/user_form.html', {'form': form, 'operation': 'editing'})
        return render(request, 'user/user_by_id.html', {'user_by_id': user})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.get_by_id(id)
            if user is None:
                raise ObjectDoesNotExist
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'user/user_form.html', {'form': form})
        return redirect('user_list')


# Create your views here.

def user_by_id(request, id=0):
    user_by_id = CustomUser.objects.get(id=id)
    return render(request, 'user/user_by_id.html', {'title': "User by id", "user_by_id": user_by_id})


def user_delete(request, id=0):
    user = CustomUser.get_by_id(id)
    if user is None:
        raise FileNotFoundError
    user.delete()
    return redirect('user_list')




def user_by_id(request, id=0):
    user_by_id = CustomUser.objects.get(id=id)
    return render(request, 'user/user_by_id.html', {'title': "User by id", "user_by_id": user_by_id})


def user_update(request):
    # def book_update(request, book_id=0, name, description, author, count):
    # if name:
    #     Book.objects.get(id=book_id).name = name
    # if description:
    #     Book.objects.get(id=book_id).description = description
    # if author:
    #     Book.objects.get(id=book_id).author = author
    # if count:
    #     Book.objects.get(id=book_id).count = count
    # Book.save()
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})


def user_delete(request, id=0):
    user = CustomUser.objects.get(id=id)
    user.delete()
    users = list(CustomUser.objects.all())
    return render(request, 'user/all_users.html', {'title': "All users", "users": users})

