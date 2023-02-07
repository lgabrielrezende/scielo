from django.db import models


class Journal(models.Model):
    journal_id = models.CharField(max_length=50)
    title = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Author(models.Model):
    author_id = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    given_names = models.CharField(max_length=100)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.surname


class Article(models.Model):
    article_id = models.CharField(max_length=50)
    title = models.TextField(blank=False, null=False)
    volume = models.IntegerField(blank=False, null=False)
    publication_year_date = models.IntegerField(blank=False, null=False)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Figure(models.Model):
    figure_id = models.CharField(max_length=10)
    fig_type = models.CharField(max_length=15)
    figure_language = models.CharField(max_length=10)
    orientation = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    label = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Graphic(models.Model):
    href = models.CharField(max_length=1000)
    content_type = models.CharField(max_length=15)
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.href
