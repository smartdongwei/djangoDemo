from django.contrib import admin

# Register your models here.
from django.http import HttpResponse
from books.models import Publisher,Author,Book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name','email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    search_fields = ('title','publisher','publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')
    search_fields = ('name','website')

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


