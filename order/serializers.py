from rest_framework import serializers
from .models import Order, Author
from book.serializers import BookListSerializer


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    book = BookListSerializer(read_only=True)
    # authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ('user', 'book', 'created_at', 'end_at', 'plated_end_at')
        # fields = '__all__'
