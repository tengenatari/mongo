from djongo import models

from djongo.models import ObjectIdField, ArrayField


class Book(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    attributes = models.JSONField()

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._id


class Reader(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    books = ArrayField(Book)

    attributes = models.JSONField()

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._id

