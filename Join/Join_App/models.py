from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=255, unique=True) 

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    #assigned = assignedContacts;
    date = models.DateField()
    prio = models.BooleanField(default=False)
    #category = 

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = PhoneNumberField(unique=True, region="DE")

    def __str__(self):
        f"{self.name}, {self.email}"