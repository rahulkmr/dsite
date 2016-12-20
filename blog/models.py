from django.db import models

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
    PAGE_LIMIT = 4

    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField('Published', auto_now_add=True)
    mod_date = models.DateTimeField('Modified', auto_now=True)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)
    n_comments = models.IntegerField('number of comments', default=0)
    n_pingbacks = models.IntegerField('number of pingbacks', default=0)
    rating = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'entries'
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']

    def __str__(self):
        return self.headline


class Comment(models.Model):
    entry = models.ForeignKey(Entry)
    commenter = models.CharField(max_length=100)
    comment = models.TextField()
    pub_date = models.DateTimeField('Commented on', auto_now_add=True)
