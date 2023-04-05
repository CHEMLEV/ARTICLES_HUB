from django.db import models


class ArticleCategory(models.Model):

    category_id = models.IntegerField
    category_name = models.TextField(max_length=255)
    

class ArticleType(models.Model):

    type_id = models.IntegerField
    type_name = models.TextField(max_length=255)
    
class Article (models.Model):

    article_id = models.IntegerField
    type_id = models.ForeignKey (ArticleType, on_delete=models.SET_NULL, null=True)
    category_id = models.ForeignKey (ArticleCategory, on_delete=models.SET_NULL, null=True)
    article_name = models.TextField(max_length=255)
    born = models.DateField
    died = models.DateField
    nationality = models.TextField(max_length=50)
    notable_work = models.TextField(max_length=255)
    about = models.TextField
    known_for = models.TextField(max_length=255)
    year = models.DateField
    medium = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    designed = models.TextField(max_length=255)
    developer = models.TextField(max_length=255)









