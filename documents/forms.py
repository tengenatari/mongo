from django import forms
from documents.models import *


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['name', 'age', 'gender', 'address', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        super(ReaderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    def clean(self):
        cleaned_data = super(ReaderForm, self).clean()
        self.instance.attributes = {}

        return cleaned_data


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'author', 'pages', 'year']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        self.instance.attributes = {}

        return cleaned_data

