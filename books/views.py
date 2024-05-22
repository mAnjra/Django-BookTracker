from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Books
from .forms import BookForm



def index(request):
    return render(request, 'index.html')

@login_required
def books(request):
    '''Displays Books from all 3 sections, Library, Currently Reading, Completed'''
    library_books = Books.objects.filter(owner=request.user, status='library')
    reading_books = Books.objects.filter(owner=request.user, status='reading')
    completed_books = Books.objects.filter(owner=request.user, status='completed')
    #mybooks = Books.objects.filter(book_title__startswith='D') field lookups all start with two underscores
    #mybooks = Books.objects.filter(book_title='Deep Work').values()
    
    context = {
        'library_books': library_books,
        'reading_books': reading_books,
        'completed_books': completed_books
    }
    return render(request, 'all_books.html', context)

@login_required
def book_details(request, id):
    mybooks = Books.objects.get(id=id)
    if mybooks.owner != request.user:
        raise Http404
    #template = loader.get_template('details.html')
    context = {'mybooks':mybooks}
    return render(request, 'details.html', context)

@login_required
def add_book(request):
    if request.method != "POST":
        form = BookForm()
    else:
        # create a form instance and populate it with the info requests carries
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()
            return redirect('books:books')
    context= {'form':form}
    return render(request, 'add_book.html', context)

@login_required
def delete_book(request, book_id):
    """Deletes book and returns to all books page"""
    book = Books.objects.get(id=book_id).delete()
    return redirect('books:books')

@login_required
def completed_book(request, book_id):
    '''Updates completed book field with todays date and updates status to completed book'''
    book = Books.objects.get(id=book_id)   
    book.status = 'completed'
    book.completed_date = timezone.now().date()
    book.save()
    return redirect('books:books')

@login_required
def reading_book(request, book_id):
    '''Updates book with status reading book'''
    book = Books.objects.get(id=book_id)
    book.status = 'reading'
    if book.start_date is None:
        book.start_date = timezone.now().date()
    book.save()
    return redirect('books:books')

@login_required
def add_library(request, book_id):
    """Adds book to library in cases where its status was chnaged by mistake"""
    book = Books.objects.get(id=book_id)
    book.status = 'library'
    book.completed_date = None
    book.save()
    return redirect('books:books')

@login_required
def edit_book(request, book_id):
    """Editing book data"""
    book = Books.objects.get(id=book_id)

    if request.method != "POST":
        form = BookForm(instance=book)
    else:
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:details', id=book_id)
    
    context = {'form':form,'book':book}
    return render(request, 'edit_book.html', context) 