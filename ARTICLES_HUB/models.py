from django.db import models


class ArticleCategory(models.Model):

    category_id = models.IntegerField
    category_name = models.TextField(max_length=255)

    def __str__(self):
        return self.category_name
    

class ArticleType(models.Model):

    type_id = models.IntegerField
    type_name = models.TextField(max_length=255)

    def __str__(self):
        return self.type_name
    

class Article (models.Model):

    article_id = models.IntegerField
    type_id = models.ForeignKey (ArticleType, on_delete=models.SET_NULL, null=True)
    category_id = models.ForeignKey (ArticleCategory, on_delete=models.SET_NULL, null=True)
    article_name = models.TextField(max_length=255)
    year_of_born = models.TextField(max_length=50, blank=True)
    year_of_died = models.TextField(max_length=50, blank=True)
    nationality = models.TextField(max_length=50, blank=True)
    notable_work = models.TextField(max_length=255, blank=True)
    article_about = models.TextField(max_length=8000, blank=True)
    known_for = models.TextField(max_length=255, blank=True)
    article_year = models.TextField(max_length=50, blank=True)
    medium = models.TextField(max_length=255, blank=True)
    dimensions = models.TextField(max_length=255, blank=True)
    location = models.TextField(max_length=255, blank=True)
    designed = models.TextField(max_length=255, blank=True)
    developer = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.article_name
    









