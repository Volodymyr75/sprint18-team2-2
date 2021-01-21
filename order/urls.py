from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_orders, name='orders'),
    path('<int:id>/update', views.update_by_id, name='update_by_id'),
    path('<int:id>/', views.order_by_id, name='order_by_id'),
    path('<int:id>/delete/', views.order_delete, name='order_delete'),
]
