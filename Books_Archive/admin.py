from django.contrib import admin
from .models import Books, Author
from django.http import HttpResponse
import csv

# Register your models here.

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected Books"

admin.site.register(Author)
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ["title", "author", "verified"]
    list_filter = ["author"]
    list_editable = ["verified"]
    actions = ['export_as_csv']

admin.site.site_header = 'ChristianBooks Bot administration'
