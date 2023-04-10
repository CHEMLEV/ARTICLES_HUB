from django import forms
from .models import ArticleCategory, ArticleType, Article
import django_filters
 

class ArticleFilter(django_filters.FilterSet):

    article_name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'filter_field'})) 
      

    category_id = django_filters.ModelChoiceFilter(
        queryset=ArticleCategory.objects.all(),
        empty_label="All Categories",
        label="Categories",
        widget=forms.Select(attrs={'class': 'filter_field'}),
        )


    class Meta:
        model = Article
        fields = ['category_id', 'article_name'] #'__all__'

