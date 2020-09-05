from django.contrib.admin import site, ModelAdmin
from books.models import Book


class BookModelAdmin(ModelAdmin):
    list_display = ["name", "author", "year"]
    search_fields = ["name", "author"]
    list_filter = ["year"]


site.register(Book, BookModelAdmin)
