from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:id>/update', views.update_by_id, name='update_by_id'),
    path('<int:id>/', views.book_by_id, name='book_by_id'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),
]