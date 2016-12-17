from django.contrib import admin

from .models import Blog, Author, Entry

admin.site.register(Author)
admin.site.register(Blog)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'mod_date',)
    list_filter = ('pub_date', 'authors', 'rating')
    fields = (('blog', 'headline'), 'body_text', 'authors', ('pub_date', 'mod_date'),
              ('n_comments', 'n_pingbacks', 'rating'))
    date_hierarchy = 'pub_date'
    search_fields = ('headline', 'authors__name', 'authors__email')
