from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Entry


class EntryListView(ListView):
    model = Entry
    paginate_by = Entry.PAGE_LIMIT



class EntryDetailView(DetailView):
    model = Entry
