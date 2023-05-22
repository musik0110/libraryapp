import time
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, Author, Publisher
from .forms import AddPublisherForm, AddBookForm, AddAuthorForm
# Create your views here.


def books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 1)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'all_books.html', {'books': page_object})


def book_detail(request, id):
    book = Book.objects.get(id=id)
    formatted_date = book.publication_date.strftime("%Y-%m-%d")
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'book_detail.html', {'book': book, 'authors': authors, 'publishers': publishers, 'date': formatted_date})


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddBookForm()
    return render(request, 'add_data.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddAuthorForm()
    return render(request, 'add_data.html', {'form': form})


def add_publisher(request):
    if request.method == 'POST':
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = AddPublisherForm()
    return render(request, 'add_data.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all_books')
        else:
            return HttpResponse('Неправильные учетные данные')

    return render(request, 'login.html')


def update_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = Author.objects.get(id=request.POST.get('author_id'))
        book.publisher = Publisher.objects.get(id=request.POST.get('publisher_id'))
        book.publication_date = request.POST.get('publication_date')

        cover_photo = request.FILES.get('cover_photo')
        if cover_photo:
            filename = '{}_{}'.format(int(time.time()), cover_photo.name)
            filepath = default_storage.save('media/' + filename, cover_photo)
            book.cover_photo = filepath

        book.save()
        return redirect('book_detail', id=id)
