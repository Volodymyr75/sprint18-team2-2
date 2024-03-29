from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_form, name='author_insert'),
    path('<int:id>/', views.author_form, name='author_view'),
    path('edit/<int:id>', views.author_form, name='author_update'),
    path('delete/<int:id>', views.author_delete, name='author_delete'),
    path('list/', views.author_list, name='author_list'),
]
