import django.forms
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter', 'comment', 'entry']
        widgets = {'entry': django.forms.HiddenInput()}
