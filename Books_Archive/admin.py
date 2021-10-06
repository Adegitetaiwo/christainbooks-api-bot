from django.contrib import admin
from .models import Books, Author

# Register your models here.
admin.site.register(Author)
admin.site.register(Books)
