from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.name
