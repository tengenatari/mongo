from django.shortcuts import render

from documents.forms import ReaderForm, BookForm
from documents.models import Reader, Book
from djongo.models.fields import ObjectId, ArrayField
# Create your views here.


def index(request):

    return render(request, 'documents/base.html', {'readers': Reader.objects.all()})


def create_reader(request, instance_id):
    form = ReaderForm()
    book_forms = []
    instance = {}
    if request.method == 'POST':
        if instance_id == "0":
            form = ReaderForm(request.POST)
            form.save(commit=True)

    if instance_id != "0":
        instance = Reader.objects.get(_id=ObjectId(instance_id))
        form = ReaderForm(instance=instance)

        books = instance.books
        book_forms = []
        if books:
            for book in books:
                book_forms.append(BookForm(instance=Book.objects.get(_id=ObjectId(book['_id']))))
    return render(request, 'documents/create_reader.html', context={'form': form, 'book_form': BookForm(), 'books': book_forms, "instance": instance})


def insert_book(request, instance_id):
    instance = Reader.objects.get(_id=ObjectId(instance_id))
    form = BookForm(request.POST).save()
    if instance.books:
        instance.books.append(Book.objects.get(_id=ObjectId(form.id)).__dict__)
    else:
        instance.books = [Book.objects.get(_id=ObjectId(form.id)).__dict__]
    instance.save()


def update_reader(request):
    form = ReaderForm()

    if request.method == 'POST':
        form = ReaderForm(request.POST)
        form.save(commit=True)

    return render(request, 'documents/create_reader.html', context={'form': form})
