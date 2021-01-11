from django.contrib import admin

# Register your models here.
from libraryapp import models

admin.site.register(models.Book)
