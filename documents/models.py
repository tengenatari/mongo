from djongo import models

from djongo.models import ObjectIdField, ArrayField


class Ticket(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    attributes = models.JSONField()

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._id


class Reader(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    attributes = models.JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self._id
