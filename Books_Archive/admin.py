from django.contrib import admin
from .models import Books, Author

# Register your models here.
admin.site.register(Author)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    list_filter = ["author"]
