from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    #Hidden
    password = models.TextField()
    primary_token = models.TextField(null=True, blank=True)
    secondary_token = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    verified = models.BooleanField()
    #Hidden
    #Auto
    deleted = models.DateTimeField(null=True, blank=True)
    #Auto
    modified = models.DateTimeField()
    #Auto
    created = models.DateTimeField()

