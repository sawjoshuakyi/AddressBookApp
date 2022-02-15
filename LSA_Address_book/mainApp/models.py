import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contactlist", null = True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    contactlist = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    homephoneNumber = models.CharField(max_length=200)
    workphoneNumber = models.CharField(max_length=200)
    mobilephoneNumber = models.CharField(max_length=200)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName
