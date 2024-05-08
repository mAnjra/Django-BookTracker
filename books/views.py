from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Books
from .forms import BookForm



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def books(request):
    '''Displays Books from all 3 sections, Library, Currently Reading, Completed'''
    mybooks = Books.objects.all().values()
    library_books = Books.objects.filter(status='library')
    reading_books = Books.objects.filter(status='reading')
    completed_books = Books.objects.filter(status='completed')
    #mybooks = Books.objects.filter(book_title__startswith='D') field lookups all start with two underscores
    #mybooks = Books.objects.filter(book_title='Deep Work').values()
    template = loader.get_template('all_books.html')

    context = {
        'library_books': library_books,
        'reading_books': reading_books,
        'completed_books': completed_books
    }
    return HttpResponse(template.render(context, request))

def book_details(request, id):
    mybooks = Books.objects.get(id=id)
    #template = loader.get_template('details.html')
    context = {'mybooks':mybooks}
    return render(request, 'details.html', context)

def add_book(request):
    if request.method != "POST":
        form = BookForm()
    else:
        # create a form instance and populate it with the info requests carries
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.save()
            return redirect('books')
    context= {'form':form}
    return render(request, 'add_book.html', context)

def delete_book(request, book_id):
    """Deletes book and returns to all books page"""
    book = Books.objects.get(id=book_id).delete()
    return redirect('books')

def completed_book(request, book_id):
    '''Updates completed book field with todays date and updates status to completed book'''
    book = Books.objects.get(id=book_id)   
    book.status = 'completed'
    book.completed_date = timezone.now().date()
    book.save()
    return redirect('books')

def reading_book(request, book_id):
    '''Updates book with status reading book'''
    book = Books.objects.get(id=book_id)
    book.status = 'reading'
    book.start_date = timezone.now().date()
    book.save()
    return redirect('books')


 

