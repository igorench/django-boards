#  this is a configuration file for a built-in Django app called
# Django Admin
from django.contrib import admin
from .models import Board

# Register your models here.

admin.site.register(Board)
