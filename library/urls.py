from django.urls import path
from library import views

urlpatterns = [
    path('books/', views.book_list),   
]
