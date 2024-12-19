from django import forms
from documents.models import *


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['name', 'phone']

    def __init__(self, *args, attributes=None, **kwargs):
        super(ReaderForm, self).__init__(*args, **kwargs)
        if attributes is None:
            attributes = dict()
        self.my_attributes = attributes
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    def clean(self):
        cleaned_data = super().clean()
        attributes = dict()

        for key, value in self.my_attributes.items():
            print(key, value)
            attributes[key] = value
        self.instance.attributes = attributes
        self.instance.save()

        return cleaned_data


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'age']

    def __init__(self, *args, attributes=None, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        if attributes is None:
            attributes = dict()
        self.my_attributes = attributes
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    def clean(self):
        cleaned_data = super().clean()
        attributes = dict()

        for key, value in self.my_attributes.items():
            print(key, value)
            attributes[key] = value
        self.instance.attributes = attributes
        self.instance.save()

        return cleaned_data



