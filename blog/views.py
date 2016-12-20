from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Entry


class EntryListView(ListView):
    model = Entry
