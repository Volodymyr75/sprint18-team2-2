from django.urls import path, include
from .views_rest_api import OrderCreateView, OrderListView, OrderDetailView

urlpatterns = [
    path('create', OrderCreateView.as_view()),
    path('all', OrderListView.as_view()),
    path('detail/<int:pk>/', OrderDetailView.as_view())
    ]