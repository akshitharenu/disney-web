from django.contrib import admin
from .models import movie,customer,Book
# Register your models here.
admin.site.register(movie)
admin.site.register(customer)
admin.site.register(Book)