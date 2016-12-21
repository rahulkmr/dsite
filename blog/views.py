from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Entry, Comment
from .forms import CommentForm


class EntryListView(ListView):
    model = Entry
    paginate_by = Entry.PAGE_LIMIT



class EntryDetailView(DetailView):
    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'entry': context['object'].id})
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['commenter', 'comment', 'entry']
