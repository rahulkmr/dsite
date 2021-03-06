from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.EntryListView.as_view(), name='index'),
    url(r'^(?P<pk>.+)/$', views.EntryDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>.+)/comment_add$', views.CommentCreateView.as_view(), name='comment_add'),
]
