from django.shortcuts import render, redirect
from .models import Order
from django.core.exceptions import ObjectDoesNotExist
from .forms import OrderForms


# def all_orders(request):
#     orders = list(Order.objects.all())
#     return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})

def all_orders(request):
    orders = list(Order.objects.all())
    context = {'orders': orders}
    return render(request, 'order/all_orders.html', context)


# Create your views here.

def order_by_id(request, id=0):
    order_by_id = Order.objects.get(id=id)
    return render(request, 'order/order_by_id.html', {'title': "Order by ID", "order_by_id": order_by_id})


# def order_update(request):
#     # def book_update(request, book_id=0, name, description, author, count):
#     # if name:
#     #     Book.objects.get(id=book_id).name = name
#     # if description:
#     #     Book.objects.get(id=book_id).description = description
#     # if author:
#     #     Book.objects.get(id=book_id).author = author
#     # if count:
#     #     Book.objects.get(id=book_id).count = count
#     # Book.save()
#     orders = list(Order.objects.all())
#     return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})

def update_by_id(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = OrderForms()
        else:
            book = Order.objects.get(pk=id)
            form = OrderForms(instance=book)
        return render(request, 'order/update_by_id.html', {'form': form})

    if request.method == 'POST':
        if id == 0:
            form = OrderForms(request.POST)
        else:
            book = Order.objects.get(pk=id)
            form = OrderForms(request.POST, instance=book)
        form.save()
        return redirect('orders')


# def order_delete(request, id=0):
#     order = Order.objects.get(id=id)
#     order.delete()
#     # Book.save()
#     orders = list(Order.objects.all())
#     return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})

def order_delete(request, id=0):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('orders')
