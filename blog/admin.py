from django.contrib import admin

from .models import Blog, Author, Entry, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'mod_date',)
    list_filter = ('pub_date', 'rating')
    fields = (('blog', 'headline'), 'body_text', ('authors', 'tags'),
              ('pub_date', 'mod_date'),
              ('n_comments', 'n_pingbacks', 'rating'))
    date_hierarchy = 'pub_date'
    search_fields = ('headline', 'authors__name', 'authors__email')
