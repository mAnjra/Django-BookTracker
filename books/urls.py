from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books,  name='books'),
    path('details/<int:id>', views.book_details, name='details'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('delete_book/<book_id>', views.delete_book, name='delete_book'),
    path('add_to_completed/<book_id>', views.completed_book, name='completed_book'),
    path('add_to_reading/<book_id>', views.reading_book, name='reading_book'),
    path('add_to_library/<book_id>', views.add_library, name='add_library'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),

]