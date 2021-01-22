from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderDetailSerializer, OrderListSerializer
from .models import Order

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()