from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
)

class Profiles(models.Model):
    Prefix = models.CharField(max_length=60, default="", blank=True, null=False,choices=TYPE_CHOICES)
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.CharField(max_length=60, default="", blank=True, null=False)
    Username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name

