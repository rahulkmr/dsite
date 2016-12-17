from django.db import models
from django.utils import timezone

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField('Published', default=timezone.now)
    mod_date = models.DateTimeField('Modified', default=timezone.now)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField('number of comments', default=0)
    n_pingbacks = models.IntegerField('number of pingbacks', default=0)
    rating = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'entries'
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']

    def __str__(self):
        return self.headline
