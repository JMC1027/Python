from django.contrib import admin

from .models import DjangoClasses
#Importing DjangoClasses from the models .py folder
admin.site.register(DjangoClasses)
