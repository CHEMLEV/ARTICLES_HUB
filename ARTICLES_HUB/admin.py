from django.contrib import admin
from .models import ArticleCategory, ArticleType, Article

# Register your models here.
admin.site.register(ArticleCategory)
admin.site.register(ArticleType)
admin.site.register(Article)

