from django.contrib import admin
from .models import Books

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title','book_genre','start_date','completed_date')

admin.site.register(Books, BookAdmin)
