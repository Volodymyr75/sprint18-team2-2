from django.urls import path, include
from .views_rest_api import BookCreateView

urlpatterns = [
    path('create', BookCreateView.as_view())
]