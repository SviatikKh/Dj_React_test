from django.core.validators import validate_email
from django.db import models


class Group(models.Model):
    name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group,blank=True, null=True)

    def __str__(self):
        return self.name

    
